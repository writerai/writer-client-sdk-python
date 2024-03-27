"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import base64
import json
import re
import sys
from dataclasses import Field, fields, is_dataclass, make_dataclass
from datetime import date, datetime
from decimal import Decimal
from email.message import Message
from enum import Enum
from typing import (Any, Callable, Dict, List, Optional, Tuple, Union,
                    get_args, get_origin)
from xmlrpc.client import boolean
from typing_inspect import is_optional_type
import dateutil.parser
from dataclasses_json import DataClassJsonMixin


def get_security(security: Any) -> Tuple[Dict[str, str], Dict[str, str]]:
    headers: Dict[str, str] = {}
    query_params: Dict[str, str] = {}

    if security is None:
        return headers, query_params

    sec_fields: Tuple[Field, ...] = fields(security)
    for sec_field in sec_fields:
        value = getattr(security, sec_field.name)
        if value is None:
            continue

        metadata = sec_field.metadata.get('security')
        if metadata is None:
            continue
        if metadata.get('option'):
            _parse_security_option(headers, query_params, value)
            return headers, query_params
        if metadata.get('scheme'):
            # Special case for basic auth which could be a flattened struct
            if metadata.get("sub_type") == "basic" and not is_dataclass(value):
                _parse_security_scheme(headers, query_params, metadata, security)
            else:
                _parse_security_scheme(headers, query_params, metadata, value)

    return headers, query_params


def _parse_security_option(headers: Dict[str, str], query_params: Dict[str, str], option: Any):
    opt_fields: Tuple[Field, ...] = fields(option)
    for opt_field in opt_fields:
        metadata = opt_field.metadata.get('security')
        if metadata is None or metadata.get('scheme') is None:
            continue
        _parse_security_scheme(
            headers, query_params, metadata, getattr(option, opt_field.name))


def _parse_security_scheme(headers: Dict[str, str], query_params: Dict[str, str], scheme_metadata: Dict, scheme: Any):
    scheme_type = scheme_metadata.get('type')
    sub_type = scheme_metadata.get('sub_type')

    if is_dataclass(scheme):
        if scheme_type == 'http' and sub_type == 'basic':
            _parse_basic_auth_scheme(headers, scheme)
            return

        scheme_fields: Tuple[Field, ...] = fields(scheme)
        for scheme_field in scheme_fields:
            metadata = scheme_field.metadata.get('security')
            if metadata is None or metadata.get('field_name') is None:
                continue

            value = getattr(scheme, scheme_field.name)

            _parse_security_scheme_value(
                headers, query_params, scheme_metadata, metadata, value)
    else:
        _parse_security_scheme_value(
            headers, query_params, scheme_metadata, scheme_metadata, scheme)


def _parse_security_scheme_value(headers: Dict[str, str], query_params: Dict[str, str], scheme_metadata: Dict, security_metadata: Dict, value: Any):
    scheme_type = scheme_metadata.get('type')
    sub_type = scheme_metadata.get('sub_type')

    header_name = str(security_metadata.get('field_name'))

    if scheme_type == "apiKey":
        if sub_type == 'header':
            headers[header_name] = value
        elif sub_type == 'query':
            query_params[header_name] = value
        else:
            raise Exception('not supported')
    elif scheme_type == "openIdConnect":
        headers[header_name] = _apply_bearer(value)
    elif scheme_type == 'oauth2':
        if sub_type != 'client_credentials':
            headers[header_name] = _apply_bearer(value)
    elif scheme_type == 'http':
        if sub_type == 'bearer':
            headers[header_name] = _apply_bearer(value)
        else:
            raise Exception('not supported')
    else:
        raise Exception('not supported')


def _apply_bearer(token: str) -> str:
    return token.lower().startswith('bearer ') and token or f'Bearer {token}'


def _parse_basic_auth_scheme(headers: Dict[str, str], scheme: Any):
    username = ""
    password = ""

    scheme_fields: Tuple[Field, ...] = fields(scheme)
    for scheme_field in scheme_fields:
        metadata = scheme_field.metadata.get('security')
        if metadata is None or metadata.get('field_name') is None:
            continue

        field_name = metadata.get('field_name')
        value = getattr(scheme, scheme_field.name)

        if field_name == 'username':
            username = value
        if field_name == 'password':
            password = value

    data = f'{username}:{password}'.encode()
    headers['Authorization'] = f'Basic {base64.b64encode(data).decode()}'


def generate_url(clazz: type, server_url: str, path: str, path_params: Any,
                 gbls: Optional[Dict[str, Dict[str, Dict[str, Any]]]] = None) -> str:
    path_param_fields: Tuple[Field, ...] = fields(clazz)
    for field in path_param_fields:
        request_metadata = field.metadata.get('request')
        if request_metadata is not None:
            continue

        param_metadata = field.metadata.get('path_param')
        if param_metadata is None:
            continue

        param = getattr(
            path_params, field.name) if path_params is not None else None
        param = _populate_from_globals(
            field.name, param, 'pathParam', gbls)

        if param is None:
            continue

        f_name = param_metadata.get("field_name", field.name)
        serialization = param_metadata.get('serialization', '')
        if serialization != '':
            serialized_params = _get_serialized_params(
                param_metadata, field.type, f_name, param)
            for key, value in serialized_params.items():
                path = path.replace(
                    '{' + key + '}', value, 1)
        else:
            if param_metadata.get('style', 'simple') == 'simple':
                if isinstance(param, List):
                    pp_vals: List[str] = []
                    for pp_val in param:
                        if pp_val is None:
                            continue
                        pp_vals.append(_val_to_string(pp_val))
                    path = path.replace(
                        '{' + param_metadata.get('field_name', field.name) + '}', ",".join(pp_vals), 1)
                elif isinstance(param, Dict):
                    pp_vals: List[str] = []
                    for pp_key in param:
                        if param[pp_key] is None:
                            continue
                        if param_metadata.get('explode'):
                            pp_vals.append(
                                f"{pp_key}={_val_to_string(param[pp_key])}")
                        else:
                            pp_vals.append(
                                f"{pp_key},{_val_to_string(param[pp_key])}")
                    path = path.replace(
                        '{' + param_metadata.get('field_name', field.name) + '}', ",".join(pp_vals), 1)
                elif not isinstance(param, (str, int, float, complex, bool, Decimal)):
                    pp_vals: List[str] = []
                    param_fields: Tuple[Field, ...] = fields(param)
                    for param_field in param_fields:
                        param_value_metadata = param_field.metadata.get(
                            'path_param')
                        if not param_value_metadata:
                            continue

                        parm_name = param_value_metadata.get(
                            'field_name', field.name)

                        param_field_val = getattr(param, param_field.name)
                        if param_field_val is None:
                            continue
                        if param_metadata.get('explode'):
                            pp_vals.append(
                                f"{parm_name}={_val_to_string(param_field_val)}")
                        else:
                            pp_vals.append(
                                f"{parm_name},{_val_to_string(param_field_val)}")
                    path = path.replace(
                        '{' + param_metadata.get('field_name', field.name) + '}', ",".join(pp_vals), 1)
                else:
                    path = path.replace(
                        '{' + param_metadata.get('field_name', field.name) + '}', _val_to_string(param), 1)

    return remove_suffix(server_url, '/') + path


def is_optional(field):
    return get_origin(field) is Union and type(None) in get_args(field)


def template_url(url_with_params: str, params: Dict[str, str]) -> str:
    for key, value in params.items():
        url_with_params = url_with_params.replace(
            '{' + key + '}', value)

    return url_with_params


def get_query_params(clazz: type, query_params: Any, gbls: Optional[Dict[str, Dict[str, Dict[str, Any]]]] = None) -> Dict[
        str, List[str]]:
    params: Dict[str, List[str]] = {}

    param_fields: Tuple[Field, ...] = fields(clazz)
    for field in param_fields:
        request_metadata = field.metadata.get('request')
        if request_metadata is not None:
            continue

        metadata = field.metadata.get('query_param')
        if not metadata:
            continue

        param_name = field.name
        value = getattr(
            query_params, param_name) if query_params is not None else None

        value = _populate_from_globals(param_name, value, 'queryParam', gbls)

        f_name = metadata.get("field_name")
        serialization = metadata.get('serialization', '')
        if serialization != '':
            serialized_parms = _get_serialized_params(
                metadata, field.type, f_name, value)
            for key, value in serialized_parms.items():
                if key in params:
                    params[key].extend(value)
                else:
                    params[key] = [value]
        else:
            style = metadata.get('style', 'form')
            if style == 'deepObject':
                params = {**params, **_get_deep_object_query_params(
                    metadata, f_name, value)}
            elif style == 'form':
                params = {**params, **_get_delimited_query_params(
                    metadata, f_name, value, ",")}
            elif style == 'pipeDelimited':
                params = {**params, **_get_delimited_query_params(
                    metadata, f_name, value, "|")}
            else:
                raise Exception('not yet implemented')
    return params


def get_headers(headers_params: Any, gbls: Optional[Dict[str, Dict[str, Dict[str, Any]]]] = None) -> Dict[str, str]:
    if headers_params is None:
        return {}

    headers: Dict[str, str] = {}

    param_fields: Tuple[Field, ...] = fields(headers_params)
    for field in param_fields:
        metadata = field.metadata.get('header')
        if not metadata:
            continue

        value = _populate_from_globals(field.name, getattr(headers_params, field.name), 'header', gbls)
        value = _serialize_header(metadata.get('explode', False), value)

        if value != '':
            headers[metadata.get('field_name', field.name)] = value

    return headers


def _get_serialized_params(metadata: Dict, field_type: type, field_name: str, obj: Any) -> Dict[str, str]:
    params: Dict[str, str] = {}

    serialization = metadata.get('serialization', '')
    if serialization == 'json':
        params[metadata.get("field_name", field_name)
               ] = marshal_json(obj, field_type)

    return params


def _get_deep_object_query_params(metadata: Dict, field_name: str, obj: Any) -> Dict[str, List[str]]:
    params: Dict[str, List[str]] = {}

    if obj is None:
        return params

    if is_dataclass(obj):
        obj_fields: Tuple[Field, ...] = fields(obj)
        for obj_field in obj_fields:
            obj_param_metadata = obj_field.metadata.get('query_param')
            if not obj_param_metadata:
                continue

            obj_val = getattr(obj, obj_field.name)
            if obj_val is None:
                continue

            if isinstance(obj_val, List):
                for val in obj_val:
                    if val is None:
                        continue

                    if params.get(
                            f'{metadata.get("field_name", field_name)}[{obj_param_metadata.get("field_name", obj_field.name)}]') is None:
                        params[
                            f'{metadata.get("field_name", field_name)}[{obj_param_metadata.get("field_name", obj_field.name)}]'] = [
                        ]

                    params[
                        f'{metadata.get("field_name", field_name)}[{obj_param_metadata.get("field_name", obj_field.name)}]'].append(
                        _val_to_string(val))
            else:
                params[
                    f'{metadata.get("field_name", field_name)}[{obj_param_metadata.get("field_name", obj_field.name)}]'] = [
                    _val_to_string(obj_val)]
    elif isinstance(obj, Dict):
        for key, value in obj.items():
            if value is None:
                continue

            if isinstance(value, List):
                for val in value:
                    if val is None:
                        continue

                    if params.get(f'{metadata.get("field_name", field_name)}[{key}]') is None:
                        params[f'{metadata.get("field_name", field_name)}[{key}]'] = [
                        ]

                    params[
                        f'{metadata.get("field_name", field_name)}[{key}]'].append(_val_to_string(val))
            else:
                params[f'{metadata.get("field_name", field_name)}[{key}]'] = [
                    _val_to_string(value)]
    return params


def _get_query_param_field_name(obj_field: Field) -> str:
    obj_param_metadata = obj_field.metadata.get('query_param')

    if not obj_param_metadata:
        return ""

    return obj_param_metadata.get("field_name", obj_field.name)


def _get_delimited_query_params(metadata: Dict, field_name: str, obj: Any, delimiter: str) -> Dict[
        str, List[str]]:
    return _populate_form(field_name, metadata.get("explode", True), obj, _get_query_param_field_name, delimiter)


SERIALIZATION_METHOD_TO_CONTENT_TYPE = {
    'json': 'application/json',
    'form': 'application/x-www-form-urlencoded',
    'multipart': 'multipart/form-data',
    'raw': 'application/octet-stream',
    'string': 'text/plain',
}


def serialize_request_body(request: Any, request_type: type, request_field_name: str, nullable: bool, optional: bool, serialization_method: str, encoder=None) -> Tuple[
        Optional[str], Optional[Any], Optional[Any]]:
    if request is None:
        if not nullable and optional:
            return None, None, None

    if not is_dataclass(request) or not hasattr(request, request_field_name):
        return serialize_content_type(request_field_name, request_type, SERIALIZATION_METHOD_TO_CONTENT_TYPE[serialization_method],
                                      request, encoder)

    request_val = getattr(request, request_field_name)

    if request_val is None:
        if not nullable and optional:
            return None, None, None

    request_fields: Tuple[Field, ...] = fields(request)
    request_metadata = None

    for field in request_fields:
        if field.name == request_field_name:
            request_metadata = field.metadata.get('request')
            break

    if request_metadata is None:
        raise Exception('invalid request type')

    return serialize_content_type(request_field_name, request_type, request_metadata.get('media_type', 'application/octet-stream'),
                                  request_val)


def serialize_content_type(field_name: str, request_type: Any, media_type: str, request: Any, encoder=None) -> Tuple[Optional[str], Optional[Any], Optional[List[List[Any]]]]:
    if re.match(r'(application|text)\/.*?\+*json.*', media_type) is not None:
        return media_type, marshal_json(request, request_type, encoder), None
    if re.match(r'multipart\/.*', media_type) is not None:
        return serialize_multipart_form(media_type, request)
    if re.match(r'application\/x-www-form-urlencoded.*', media_type) is not None:
        return media_type, serialize_form_data(field_name, request), None
    if isinstance(request, (bytes, bytearray)):
        return media_type, request, None
    if isinstance(request, str):
        return media_type, request, None

    raise Exception(
        f"invalid request body type {type(request)} for mediaType {media_type}")


def serialize_multipart_form(media_type: str, request: Any) -> Tuple[str, Any, List[List[Any]]]:
    form: List[List[Any]] = []
    request_fields = fields(request)

    for field in request_fields:
        val = getattr(request, field.name)
        if val is None:
            continue

        field_metadata = field.metadata.get('multipart_form')
        if not field_metadata:
            continue

        if field_metadata.get("file") is True:
            file_fields = fields(val)

            file_name = ""
            field_name = ""
            content = bytes()

            for file_field in file_fields:
                file_metadata = file_field.metadata.get('multipart_form')
                if file_metadata is None:
                    continue

                if file_metadata.get("content") is True:
                    content = getattr(val, file_field.name)
                else:
                    field_name = file_metadata.get(
                        "field_name", file_field.name)
                    file_name = getattr(val, file_field.name)
            if field_name == "" or file_name == "" or content == bytes():
                raise Exception('invalid multipart/form-data file')

            form.append([field_name, [file_name, content]])
        elif field_metadata.get("json") is True:
            to_append = [field_metadata.get("field_name", field.name), [
                None, marshal_json(val, field.type), "application/json"]]
            form.append(to_append)
        else:
            field_name = field_metadata.get(
                "field_name", field.name)
            if isinstance(val, List):
                for value in val:
                    if value is None:
                        continue
                    form.append(
                        [field_name + "[]", [None, _val_to_string(value)]])
            else:
                form.append([field_name, [None, _val_to_string(val)]])
    return media_type, None, form


def serialize_dict(original: Dict, explode: bool, field_name, existing: Optional[Dict[str, List[str]]]) -> Dict[
        str, List[str]]:
    if existing is None:
        existing = {}

    if explode is True:
        for key, val in original.items():
            if key not in existing:
                existing[key] = []
            existing[key].append(val)
    else:
        temp = []
        for key, val in original.items():
            temp.append(str(key))
            temp.append(str(val))
        if field_name not in existing:
            existing[field_name] = []
        existing[field_name].append(",".join(temp))
    return existing


def serialize_form_data(field_name: str, data: Any) -> Dict[str, Any]:
    form: Dict[str, List[str]] = {}

    if is_dataclass(data):
        for field in fields(data):
            val = getattr(data, field.name)
            if val is None:
                continue

            metadata = field.metadata.get('form')
            if metadata is None:
                continue

            field_name = metadata.get('field_name', field.name)

            if metadata.get('json'):
                form[field_name] = [marshal_json(val, field.type)]
            else:
                if metadata.get('style', 'form') == 'form':
                    form = {**form, **_populate_form(
                        field_name, metadata.get('explode', True), val, _get_form_field_name, ",")}
                else:
                    raise Exception(
                        f'Invalid form style for field {field.name}')
    elif isinstance(data, Dict):
        for key, value in data.items():
            form[key] = [_val_to_string(value)]
    else:
        raise Exception(f'Invalid request body type for field {field_name}')

    return form


def _get_form_field_name(obj_field: Field) -> str:
    obj_param_metadata = obj_field.metadata.get('form')

    if not obj_param_metadata:
        return ""

    return obj_param_metadata.get("field_name", obj_field.name)


def _populate_form(field_name: str, explode: boolean, obj: Any, get_field_name_func: Callable, delimiter: str) -> \
        Dict[str, List[str]]:
    params: Dict[str, List[str]] = {}

    if obj is None:
        return params

    if is_dataclass(obj):
        items = []

        obj_fields: Tuple[Field, ...] = fields(obj)
        for obj_field in obj_fields:
            obj_field_name = get_field_name_func(obj_field)
            if obj_field_name == '':
                continue

            val = getattr(obj, obj_field.name)
            if val is None:
                continue

            if explode:
                params[obj_field_name] = [_val_to_string(val)]
            else:
                items.append(
                    f'{obj_field_name}{delimiter}{_val_to_string(val)}')

        if len(items) > 0:
            params[field_name] = [delimiter.join(items)]
    elif isinstance(obj, Dict):
        items = []
        for key, value in obj.items():
            if value is None:
                continue

            if explode:
                params[key] = [_val_to_string(value)]
            else:
                items.append(f'{key}{delimiter}{_val_to_string(value)}')

        if len(items) > 0:
            params[field_name] = [delimiter.join(items)]
    elif isinstance(obj, List):
        items = []

        for value in obj:
            if value is None:
                continue

            if explode:
                if not field_name in params:
                    params[field_name] = []
                params[field_name].append(_val_to_string(value))
            else:
                items.append(_val_to_string(value))

        if len(items) > 0:
            params[field_name] = [delimiter.join(
                [str(item) for item in items])]
    else:
        params[field_name] = [_val_to_string(obj)]

    return params


def _serialize_header(explode: bool, obj: Any) -> str:
    if obj is None:
        return ''

    if is_dataclass(obj):
        items = []
        obj_fields: Tuple[Field, ...] = fields(obj)
        for obj_field in obj_fields:
            obj_param_metadata = obj_field.metadata.get('header')

            if not obj_param_metadata:
                continue

            obj_field_name = obj_param_metadata.get(
                'field_name', obj_field.name)
            if obj_field_name == '':
                continue

            val = getattr(obj, obj_field.name)
            if val is None:
                continue

            if explode:
                items.append(
                    f'{obj_field_name}={_val_to_string(val)}')
            else:
                items.append(obj_field_name)
                items.append(_val_to_string(val))

        if len(items) > 0:
            return ','.join(items)
    elif isinstance(obj, Dict):
        items = []

        for key, value in obj.items():
            if value is None:
                continue

            if explode:
                items.append(f'{key}={_val_to_string(value)}')
            else:
                items.append(key)
                items.append(_val_to_string(value))

        if len(items) > 0:
            return ','.join([str(item) for item in items])
    elif isinstance(obj, List):
        items = []

        for value in obj:
            if value is None:
                continue

            items.append(_val_to_string(value))

        if len(items) > 0:
            return ','.join(items)
    else:
        return f'{_val_to_string(obj)}'

    return ''


def unmarshal_json(data, typ, decoder=None):
    unmarshal = make_dataclass('Unmarshal', [('res', typ)],
                               bases=(DataClassJsonMixin,))
    json_dict = json.loads(data)
    try:
        out = unmarshal.from_dict({"res": json_dict})
    except AttributeError as attr_err:
        raise AttributeError(
            f'unable to unmarshal {data} as {typ} - {attr_err}') from attr_err

    return out.res if decoder is None else decoder(out.res)


def marshal_json(val, typ, encoder=None):
    if not is_optional_type(typ) and val is None:
        raise ValueError(
            f"Could not marshal None into non-optional type: {typ}")

    marshal = make_dataclass('Marshal', [('res', typ)],
                             bases=(DataClassJsonMixin,))
    marshaller = marshal(res=val)
    json_dict = marshaller.to_dict()
    val = json_dict["res"] if encoder is None else encoder(json_dict["res"])

    return json.dumps(val, separators=(',', ':'), sort_keys=True)


def match_content_type(content_type: str, pattern: str) -> boolean:
    if pattern in (content_type, "*", "*/*"):
        return True

    msg = Message()
    msg['content-type'] = content_type
    media_type = msg.get_content_type()

    if media_type == pattern:
        return True

    parts = media_type.split("/")
    if len(parts) == 2:
        if pattern in (f'{parts[0]}/*', f'*/{parts[1]}'):
            return True

    return False


def match_status_codes(status_codes: List[str], status_code: int) -> bool:
    for code in status_codes:
        if code == str(status_code):
            return True

        if code.endswith("XX") and code.startswith(str(status_code)[:1]):
            return True
    return False


def datetimeisoformat(optional: bool):
    def isoformatoptional(val):
        if optional and val is None:
            return None
        return _val_to_string(val)

    return isoformatoptional


def dateisoformat(optional: bool):
    def isoformatoptional(val):
        if optional and val is None:
            return None
        return date.isoformat(val)

    return isoformatoptional


def datefromisoformat(date_str: str):
    return dateutil.parser.parse(date_str).date()


def bigintencoder(optional: bool):
    def bigintencode(val: int):
        if optional and val is None:
            return None
        return str(val)

    return bigintencode


def bigintdecoder(val):
    if isinstance(val, float):
        raise ValueError(f"{val} is a float")
    return int(val)


def decimalencoder(optional: bool, as_str: bool):
    def decimalencode(val: Decimal):
        if optional and val is None:
            return None

        if as_str:
            return str(val)

        return float(val)

    return decimalencode


def decimaldecoder(val):
    return Decimal(str(val))


def map_encoder(optional: bool, value_encoder: Callable):
    def map_encode(val: Dict):
        if optional and val is None:
            return None

        encoded = {}
        for key, value in val.items():
            encoded[key] = value_encoder(value)

        return encoded

    return map_encode


def map_decoder(value_decoder: Callable):
    def map_decode(val: Dict):
        decoded = {}
        for key, value in val.items():
            decoded[key] = value_decoder(value)

        return decoded

    return map_decode


def list_encoder(optional: bool, value_encoder: Callable):
    def list_encode(val: List):
        if optional and val is None:
            return None

        encoded = []
        for value in val:
            encoded.append(value_encoder(value))

        return encoded

    return list_encode


def list_decoder(value_decoder: Callable):
    def list_decode(val: List):
        decoded = []
        for value in val:
            decoded.append(value_decoder(value))

        return decoded

    return list_decode


def union_encoder(all_encoders: Dict[str, Callable]):
    def selective_encoder(val: Any):
        if type(val) in all_encoders:
            return all_encoders[type(val)](val)
        return val
    return selective_encoder


def union_decoder(all_decoders: List[Callable]):
    def selective_decoder(val: Any):
        decoded = val
        for decoder in all_decoders:
            try:
                decoded = decoder(val)
                break
            except (TypeError, ValueError):
                continue
        return decoded
    return selective_decoder


def get_field_name(name):
    def override(_, _field_name=name):
        return _field_name

    return override


def _val_to_string(val) -> str:
    if isinstance(val, bool):
        return str(val).lower()
    if isinstance(val, datetime):
        return str(val.isoformat().replace('+00:00', 'Z'))
    if isinstance(val, Enum):
        return str(val.value)

    return str(val)


def _populate_from_globals(param_name: str, value: Any, param_type: str, gbls: Optional[Dict[str, Dict[str, Dict[str, Any]]]]):
    if value is None and gbls is not None:
        if 'parameters' in gbls:
            if param_type in gbls['parameters']:
                if param_name in gbls['parameters'][param_type]:
                    global_value = gbls['parameters'][param_type][param_name]
                    if global_value is not None:
                        value = global_value

    return value


def decoder_with_discriminator(field_name):
    def decode_fx(obj):
        kls = getattr(sys.modules['sdk.models'], obj[field_name])
        return unmarshal_json(json.dumps(obj), kls)
    return decode_fx


def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string

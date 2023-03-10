from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class UploadModelFileRequestFile:
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    file: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'file' }})
    

@dataclasses.dataclass
class UploadModelFileRequest:
    file: UploadModelFileRequestFile = dataclasses.field(metadata={'multipart_form': { 'file': True }})
    
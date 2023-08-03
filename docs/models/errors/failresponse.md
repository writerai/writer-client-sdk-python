# FailResponse

Bad Request


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `errors`                                                                              | list[[shared.FailMessage](../../models/shared/failmessage.md)]                        | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `extras`                                                                              | *Any*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `tpe`                                                                                 | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
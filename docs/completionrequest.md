# CompletionRequest


## Fields

| Field               | Type                | Required            | Description         | Example             |
| ------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
| `best_of`           | *Optional[int]*     | :heavy_minus_sign:  | N/A                 | 1                   |
| `frequency_penalty` | *Optional[float]*   | :heavy_minus_sign:  | N/A                 |                     |
| `logprobs`          | *Optional[int]*     | :heavy_minus_sign:  | N/A                 |                     |
| `max_tokens`        | *Optional[int]*     | :heavy_minus_sign:  | N/A                 | 1024                |
| `min_tokens`        | *Optional[int]*     | :heavy_minus_sign:  | N/A                 | 1                   |
| `n`                 | *Optional[int]*     | :heavy_minus_sign:  | N/A                 |                     |
| `presence_penalty`  | *Optional[float]*   | :heavy_minus_sign:  | N/A                 |                     |
| `prompt`            | *str*               | :heavy_check_mark:  | N/A                 |                     |
| `stop`              | List[*str*]         | :heavy_minus_sign:  | N/A                 | ["the","is","and"]  |
| `temperature`       | *Optional[float]*   | :heavy_minus_sign:  | N/A                 | 0.7                 |
| `top_p`             | *Optional[float]*   | :heavy_minus_sign:  | N/A                 | 1                   |
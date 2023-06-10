# ContinuePipelineRequestBody


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `configuration`                                            | *str*                                                      | :heavy_check_mark:                                         | A configuration string for the pipeline.                   |
| `continuation_key`                                         | *str*                                                      | :heavy_check_mark:                                         | A pipeline continuation key.                               |
| `parameters`                                               | dict[str, *Any*]                                           | :heavy_minus_sign:                                         | An object containing pipeline parameters and their values. |
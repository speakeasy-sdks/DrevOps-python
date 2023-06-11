# ListMyPipelinesResponse


## Fields

| Field                                                                                                               | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                                      | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `pipeline_list_response`                                                                                            | [Optional[ListMyPipelinesPipelineListResponse]](../../models/operations/listmypipelinespipelinelistresponse.md)     | :heavy_minus_sign:                                                                                                  | A sequence of pipelines.                                                                                            |
| `status_code`                                                                                                       | *int*                                                                                                               | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `raw_response`                                                                                                      | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                               | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `list_my_pipelines_default_application_json_object`                                                                 | [Optional[ListMyPipelinesDefaultApplicationJSON]](../../models/operations/listmypipelinesdefaultapplicationjson.md) | :heavy_minus_sign:                                                                                                  | Error response.                                                                                                     |
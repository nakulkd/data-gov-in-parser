# Data.gov.in API Interfacer v1.0 (data-gov-in-parser)

**TL;DR:** Python parser for Data.gov.in datasets accessed via API

This program was built to facilitate easier interaction with the API-enabled datasets available on the https://data.gov.in website. Some instructions before using this program:

1. Make sure your personal API key is updated in the 'api.key.txt' notepad as a single line.
2. Enter the API GET URL as mentioned in the dataset API webpage (ex: /resource/...)
3. Default format is set to json. To change the format, explicitly pass `get_format` = <format choice available on Data.gov.in for the chosen dataset>
4. For json format, the json to dict conversion feature can be used. In the function call, specify if you need this conversion as a boolean parameter.
5. Default limit is 10 as set by Data.gov.in. To modify the limit, explicitly pass `limit` = <value>.
6. Optional args for `offset` and `filter` will be included in v2.0.

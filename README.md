### Data.gov.in API Interfacer v1.0 (data-gov-in-parser)
---

**TL;DR:** Python parser for Data.gov.in datasets accessed via API

This program was built to facilitate easier interaction with the API-enabled datasets available on the https://data.gov.in website. Some instructions before using this program:

1. Make sure your personal API key is updated in the 'api.key.txt' notepad as a single line.
2. Enter the API GET URL as mentioned in the dataset API webpage (ex: /resource/...)
3. Default format is set to json. This can be changed by explicitly passing `get_format = <format choice available on Data.gov.in for the chosen dataset>`, however, the current program breaks due to the JSON > Dict > CSV setup. This will be fixed in v2.0.
4. Default limit is 10 as set by Data.gov.in. To query more entries, explicitly pass `limit = <value>`.

### Enhancements for v2.0
---

1. Inclusion of optional args for `offset` and `filter`
2. Solution for querying all records of the dataset
3. Conversion option to CSV for other downloaded formats (ex: XML)

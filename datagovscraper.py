"""
Data.gov.in API Interfacer v1.0
-------------------------------------------------------------------------------

This program was built to facilitate easier interaction with the API-enabled 
datasets available on the https://data.gov.in website. Some instructions before
using this program:

1. Make sure your personal API key is updated in the 'api.key.txt' notepad as
a single line.
2. Enter the API GET URL as mentioned in the dataset API webpage 
(ex: /resource/...)
3. Default format is set to json. To change the format, explicitly pass
`get_format` = <format choice available on Data.gov.in for the chosen dataset>
4. For json format, the json to dict conversion feature can be used. In the
function call, specify if you need this conversion as a boolean parameter.
5. Default limit is 10 as set by Data.gov.in. To modify the limit, explicitly
pass `limit` = <value>.
6. Optional args for `offset` and `filter` will be included in v2.0.

-------------------------------------------------------------------------------
"""


def DGS(url, get_format='json', limit=10):

    import requests as req

    with open('api.key.txt', mode='r') as f:
        api = f.readline()

    path = 'https://api.data.gov.in' + url

    headers = {}
    headers['api-key'] = api
    headers['format'] = get_format
    headers['limit'] = limit

    query = req.get(path, params=headers)
    assert query.status_code == 200, 'Request Failed'

    return query

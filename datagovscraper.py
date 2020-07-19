def DGS(url, get_format='json', limit=10):

    import requests as req

    with open('api.key.txt', mode='r') as f: # Read API key from the notepad
        api = f.readline()

    path = 'https://api.data.gov.in' + url # Append dataset request to the API
    
    # Build API query parameters
    headers = {}
    headers['api-key'] = api
    headers['format'] = get_format
    headers['limit'] = limit

    query = req.get(path, params=headers) # Run the query
    assert query.status_code == 200, 'Request Failed' # Test the response

    return query

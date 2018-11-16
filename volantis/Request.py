url = "https://api.volantis.io/v1/query/sync/dataset/7745b98a-baff-11e8-9e65-08d40cec20c9"
payload = "{\"queryType\":\"TEXT_SEARCH\",\"limit\":5,\"property\":\"_id\",\"objectType\":\"VERTEX\",\"objectLabel\":\"medical_status\",\"querySpec\":{\"querySpecType\":\"CONTAINS\",\"value\":\"\"}}"

response = requests.request("POST", url, data=payload, headers=header.headers)
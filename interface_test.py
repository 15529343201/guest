import requests

# 查询发布会接口
url = "http://127.0.0.1:8000/api/get_event_list/"
r = requests.get(url, params={'eid': '1'})
result = r.json()
print(result)
assert result['status'] == 200
assert result['message'] == "success"
assert result['data']['name'] == "xx 产品发布会"
assert result['data']['address'] == "北京林匹克公园水立方"
assert result['data']['start_time'] == "2016-10-15T18:00:00"

from suds.client import Client
url = "http://192.168.127.128:8000/?wsdl"
client = Client(url)
result = client.service.say_hello("bugmaster", 3)
print(result)
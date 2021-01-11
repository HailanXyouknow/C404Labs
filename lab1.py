# Python script that prints out the version of the requests library
import requests

print(requests.__version__)

request = requests.get('http://google.com/', allow_redirects=True)
print(request.status_code)
print(request.text)

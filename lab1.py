# Python script that prints out the version of the requests library
import requests

print('requests version:', requests.__version__)

request = requests.get('http://google.com/')
print('Status Code (Google):', request.status_code)

request_code = requests.get('https://raw.githubusercontent.com/HailanXyouknow/C404Labs/main/lab1.py')
print('Status Code (GitHub Source Code):', request_code.status_code)
print('Source Code (GitHub Source Code):')
print(request_code.text)

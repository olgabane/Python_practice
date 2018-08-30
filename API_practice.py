#Python API tutorial

#import requests library
import requests 
#query for ISS location
response = requests.get("http://api.open-notify.org/iss-now.json")
#get status
print response
<Response [200]>
#pring content of response
print(response.content)
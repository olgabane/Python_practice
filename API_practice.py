#Python API tutorials (Installed requests package: $sudo pip install requests)
#Tutorial used: https://www.dataquest.io/blog/python-api-tutorial/

#1. ISS location
#import requests library
import requests 
#query for ISS location
response = requests.get("http://api.open-notify.org/iss-now.json")
#get status
print response
#pring content of response
print(response.content)

#2. NYT (Installed nytimesarticle package, which access to API through python; $sudo pip install nytimesarticle)
#Tutorial used: http://dlab.berkeley.edu/blog/scraping-new-york-times-articles-python-tutorial
from nytimesarticle import articleAPI
api = articleAPI('4e605e42050a4dcab09a95d78d36b7dd')


import requests
from pprint import pprint

username = "arghya-roy"

url = f"https://api.github.com/users/{username}/repos"

user_data = requests.get(url)

pprint(user_data)


# for i in user_data:
#    if i['fork'] == True: 
#     print(i['name'])


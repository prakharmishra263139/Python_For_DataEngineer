# for API calls in python 
# Data engineer --> API (middle man to bring data from application) -----> Applications 


import requests

response  = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)

data = response.json()
print(data)
import requests

url = "http://127.0.0.1:2224/data"
response= requests.get(url)

data= response.json()

for country in data:
    print(f"""{country['name']} -- {country['country']}, 
    {country['latitude']}, {country['longitude']}""")

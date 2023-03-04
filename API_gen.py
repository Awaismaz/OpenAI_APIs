import requests


name=input('Enter Country Name: ')

response = requests.get(f'https://restcountries.com/v3.1/name/{name}')

data=response.json() #javascript object notation | Python Dictionary

# print(data[0].keys())

print(f"Capital of {name} is {data[0]['capital'][0]}")
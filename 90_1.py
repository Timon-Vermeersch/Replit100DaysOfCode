import requests , json

result = requests.get('https://icanhazdadjoke.com/', headers ={ "Accept": "application/json"})
joke = result.json()

print(json.dumps(joke, indent = 2))
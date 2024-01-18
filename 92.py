#https://www.youtube.com/watch?v=D45Z_rksCj8&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=170
import requests, json
long = '4.3517'
lat = '50.8503'
timezone = 'UTC +1'

result = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m')
user = result.json()

minimum = ''
maximum = ''
for time,temp in zip(user['hourly']['time'],user['hourly']['temperature_2m']):
    print(f"{time} , TEMP: {temp}" )
    if minimum == '':
        minimum = temp
    else:
        if temp < minimum:
            minimum = temp

    if maximum == '':
        maximum = temp
    else:
        if temp > maximum:
            maximum = temp
print(f"Min and Max temp in coming 7 days will be {minimum} and {maximum} degrees")
    
    

    
    


#print(json.dumps(user, indent=2))
import requests #to get things from network
import json #default module

city=input("enter the name of the city\n")

url=f"https://api.weatherapi.com/v1/current.json?key=471dac1c60c04d2ca11112326242305&q={city}"
r=requests.get(url)
# print(r.text)

wdic=json.loads(r.text) #it loads strings

print("Region:",wdic["location"]["region"])
print("Country:",wdic["location"]["country"])
print("Temperature in celsius:",wdic["current"]["temp_c"])
print("Temperature in Fahrenheit:",wdic["current"]["temp_f"])
print("Humidity:",wdic["current"]["humidity"])


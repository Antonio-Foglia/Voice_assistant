import requests, json
from __output__ import say
from __input__ import inp
from __recognise__ import recognise
#from __ML__ import wml
import geocoder

def weather(text):
    li=text.lower().split(' ')
    if 'in' not in li:
        #wml(li)
        x=here()
        info(x)
        return
    pos=li.index('in')
    if li[pos+1] == 'the':
        pos += 1
    i=len(li)+1
    while i > li.index(li[pos+1]):
        if place(' '.join(li[pos+1:i])) == False:
            #print(' '.join(li[pos+1:i]))
            i -= 1
        else:
            break
    if place(' '.join(li[pos+1:i])) == False:
        say('Location not found, ask again','en')
        return
    loc=' '.join(li[pos+1:i])
    #wml(li)
    x=place(loc)
    info(x)
    return

def here():
    g = geocoder.ip('me')
    o=g.latlng
    lat=o[0]
    lon=o[1]
    api_key = input('Enter your api key')
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'.format(lat,lon,api_key))
    x = response.json()
    return x


def place(loc):
    api_key = input('Enter your api key')
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + loc
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] == 200:
        return x
    else:
        return False


def info(x):
    y = x["main"]
    temperature = round(y["temp"] - 273.15,2)
    pressure = y['pressure']
    humidity = y["humidity"]
    feels_like=round(y["feels_like"] - 273.15,2)
    temp_max=round(y['temp_max']- 273.15,2)
    temp_min=round(y['temp_min']- 273.15,2)
    wind_speed=round(x["wind"]['speed']*1.94,2)
    if x["wind"]['deg'] in range(23,68):
        wind_dir='North East'
    elif x["wind"]['deg'] in range(68,113):
        wind_dir='East'
    elif x["wind"]['deg'] in range(113,158):
        wind_dir='South East'
    elif x["wind"]['deg'] in range(158,203):
        wind_dir='East'
    elif x["wind"]['deg'] in range(203,248):
        wind_dir='South West'
    elif x["wind"]['deg'] in range(248,293):
        wind_dir='West'
    elif x["wind"]['deg'] in range(293,338):
        wind_dir='North West'
    else:
        wind_dir='North'
    desc = x["weather"][0]["description"]
    loc=x["name"]
    print('##\nWeather in {}: {}\n##'.format(loc,desc))
    say('[The current weather in {} is: {}'.format(loc,desc),'en')
    say('Would you like more info?','en')
    fname=inp(3,'ques')
    text = recognise(fname)
    if 'yes' in text:
        print('## \nTemperature: {} (degrees celcius) \n-feels like: {} \n-max: {} \n-min: {} '.format(temperature,feels_like,temp_max,temp_min))
        print('Humidity: {}% \nAtmospheric pressure (in hPa unit): {} \nWind speed (knots): {} \nWind direction (deg): {} ({}erly)\n##'.format(humidity,pressure,wind_speed,x["wind"]['deg'],wind_dir))
        say('''[The temperature is {} degrees with a maximum of {} and a minimum of {}.
The humidity is {} percent and the wind is {} knots from the {}
'''.format(temperature,temp_max,temp_min,humidity,wind_speed,wind_dir),'en')
        return
    if 'no' in text:
        return

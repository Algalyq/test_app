
import requests

def weather_api(request):
    app_id = '7d4f96770bb3fa67b94ace850a66b5ce'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS =  { 'q': request,'lang':'ru', 'appid':app_id, 'units':'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    temp = res['main']['temp']
    wind = res['wind']['speed']
    cloud = res['clouds']['all']
    lon = res['coord']['lon']
    lat = res['coord']['lat']
    data = {'description': description, 'temp': temp, 'wind':wind, 'cloud':cloud,'lon':lon,'lat':lat}

    return data
import httpx
city = "Moscow,ru"
appid = '1fcf42d437cb6f743996878fc373bfcf'

response = httpx.get("http://api.openweathermap.org/data/2.5/forecast",
                        params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = response.json()

tmax = data['list'][0]['main']['temp_max']
tmin = data['list'][0]['main']['temp_min']
flike = data['list'][0]['main']['feels_like']
press = data['list'][0]['main']['pressure']

print(tmax, tmin, flike, press)


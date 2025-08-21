import requests
from datetime import datetime

def weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=f805442fe8f6e6762e260e855dd9ea6a&units=metric"
    res = requests.get(url)
    if res:
        data = res.json()
        sunrise = datetime.utcfromtimestamp(data['sys']['sunrise']).strftime('%d/%m %H:%M')
        sunset = datetime.utcfromtimestamp(data['sys']['sunset']).strftime('%d/%m %H:%M')
        datas = dict(temperature=data['main']['temp'], description=data['weather'][0]['description'],
                     humidite=data['main']['humidity'], nom= data['name'], lever_du_soleil= sunrise,
                     coucher_de_soleil= sunset, icon= data['weather'][0]['icon'])
        return datas
    else:
        raise TypeError

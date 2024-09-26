from django.shortcuts import render
import json
import requests

def weather(request):
    data = None
    error = None

    if 'city' in request.GET:
        city = request.GET.get('city')
        units = request.GET.get('units', 'metric')
        api_key = '5064b8916d1c7afc11c0d530526d30b1' 
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  
            list_of_data = response.json()
            
            if list_of_data['cod'] == 200: 
                data = {
                    "city": list_of_data['name'],
                    "country_code": str(list_of_data['sys']['country']),
                    "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
                    "temp": list_of_data['main']['temp'],
                    "humidity": str(list_of_data['main']['humidity']),
                    "pressure": str(list_of_data['main']['pressure']),
                    "wind_speed": str(list_of_data['wind']['speed']),
                    "weather_desc": list_of_data['weather'][0]['description'].capitalize(),
                }
            else:
                error = "City not found. Please try again."
        
        except requests.exceptions.RequestException:
            error = "An error occurred while retrieving the data. Please try again."

    return render(request, 'weather.html', {'data': data, 'error': error})

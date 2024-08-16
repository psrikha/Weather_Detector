from django.shortcuts import render
import json
import urllib.request

def index(request):
  if request.method == 'POST':
    city = request.POST['city']
    res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=69807c7c07caa8c2dce2b6d5b010be3b').read()
    json_data = json.loads(res)
    data = {
      "country_code": str(json_data['sys']['country']),
      "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
      "temp": str(json_data['main']['temp']) + 'k',
      "pressure": str(json_data['main']['pressure']),
      "humidity": str(json_data['main']['humidity']),

    }

  else:
    city = ''
    data = {}
  return render(request,'index.html',{'city': city,'data': data})

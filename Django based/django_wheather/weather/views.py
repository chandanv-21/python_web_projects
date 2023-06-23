from django.shortcuts import render
import json
import urllib.request
import datetime

def kelvin_to_digree(k):
            c= round(k - 273.15,2)
            return c
def time_conv(tics):
    res=datetime.datetime.utcfromtimestamp(tics)
    res_time=res.time()
    print(res_time)
    return res_time

# Create your views here.
def index(request):
    if request.method =='POST':
        city=request.POST['city']
        

        req=urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=3d6a38a95aa7e9f9598284c8c4155dc1').read()    
        json_data=json.loads(req)
        print(json_data)
        
        data={
            "country_code":json_data['sys']['country'],
            "coordinates":f"'longitude' : {json_data['coord']['lon']}, 'lattitude' : {json_data['coord']['lat']}",
            "sunrise":str(time_conv(json_data['sys']['sunrise'])) +' GMT ',
            "sunset":str(time_conv(json_data['sys']['sunset'])) +' GMT ',
            "temp":kelvin_to_digree(json_data['main']['temp']),
            "feels_like":kelvin_to_digree(json_data['main']['feels_like']),
            "temp_min":kelvin_to_digree(json_data['main']['temp_min']),
            "temp_max":kelvin_to_digree(json_data['main']['temp_max']),
            "pressure":json_data['main']['pressure'],
            "humidity":json_data['main']['humidity'],


        } 
    else:
        city=''
        data={}
    return render(request, 'index.html',{'city':city,'data':data})
from django.shortcuts import render
from django.http import HttpResponse
from .models import Favorites
from .serializers import FavoritesSerializer
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
import geocoder
# Create your views here.

@api_view(['GET',])

def getForecast(request):
    location = get_current_location()
    lat, lon = location[0]
    country=location[1]
    forecast=requests.get("http://api.openweathermap.org/data/2.5/forecast?lat="+str(lat)+"&lon="+str(lon)+"&appid="+"898aff6f7711362ca8099999882c3729&units=imperial")
   
    return Response(forecast.json())#-
   
#+
def weather_api():#+
    # Add your weather API implementation here#+
    pass#+

@api_view(['GET','PUT'])
def getCurrentWeather(request):
    if(request.data):

        try:
            lat = request.data.lat
            lon=request.data.lng
        except:
            lat=request.data['lat']
            lon=request.data['lon']

        current=requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(lon)+"&appid="+"898aff6f7711362ca8099999882c3729&units=imperial")
        return Response(current.json())

    else:
        print(request.data,"Get current weather")
        location = get_current_location()
        lat, lon = location[0]
        current=requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(lon)+"&appid="+"898aff6f7711362ca8099999882c3729&units=imperial")
        return Response(current.json())



def get_current_location():
    g = geocoder.ip('me')
    if g.ok:
        return g.latlng, g.address
    else:
        return None



@api_view(['GET',])
def getFavorites(request):

    favorites=Favorites.objects.all()
    serializer=FavoritesSerializer(favorites,many=True)

    return Response(serializer.data)

@api_view(['PUT',])
def updateForecast(request):
    data=request.data['coord']
    forecast=requests.get("http://api.openweathermap.org/data/2.5/forecast?lat="+str(data['lat'])+"&lon="+str(data['lon'])+"&appid="+"898aff6f7711362ca8099999882c3729&units=imperial")
    return Response(forecast.json())

@api_view(['PUT',])
def updateLocation(request):
    data=request.data

    current=requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+str(data['lat'])+"&lon="+str(data['lng'])+"&appid="+"898aff6f7711362ca8099999882c3729&units=imperial")

    return Response(current.json())

@api_view(['PUT',])
def addFavorite(request):
    data=request.data
    favorite=Favorites(favorites=data['name'],country=data['sys']['country'],favoritesdata=data['coord'])
    favorite.save()
    favorite=Favorites.objects.all()
    # favorite.delete()
    # for i in favorite:
    #    print(i.favoritesdata,"fafa")
    return Response(status=201)



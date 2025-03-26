from django.urls import path
from . import views

urlpatterns = [
     path("",views.getCurrentWeather,name="current"),
     path("forecast",views.getForecast,name="forecast"),
     path("favorites",views.getFavorites,name="favorites"),
     path("forecastUpdate",views.updateForecast,name="forecastUpdate"),
     path("searchLocation",views.updateLocation,name="locationUpdate"),
     path("favoritesAdd",views.addFavorite,name="favoritesAdd"),
          # path("favoritesDelete",views.deleteFavorite,name="favoritesDelete"),
]

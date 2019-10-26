from apis.views import menu
from .views import weather
from django.urls import path
urlpatterns = [
    path('weather', weather.hello_word),
    path('menu', menu.get_menu),
]
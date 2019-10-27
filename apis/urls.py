from apis.views import menu, image
from .views import weather
from django.urls import path
urlpatterns = [
    path('weather', weather.hello_word),
    path('menu', menu.get_menu),
    path('image', image.image),
    path('imagetext', image.image_text),
]
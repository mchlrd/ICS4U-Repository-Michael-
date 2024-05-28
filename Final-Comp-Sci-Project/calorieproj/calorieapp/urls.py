from django.urls import path
from . import views

urlpatterns = [
    path('calorieCounter', views.calorieCounter, name='calorieCounter'),
    path('', views.welcome, name='welcome')
]

from django.urls import path
from . import views

urlpatterns = [
    path('calorieCounter/', views.calorieCounter, name='calorieCounter'),
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('support/', views.support, name='support'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]

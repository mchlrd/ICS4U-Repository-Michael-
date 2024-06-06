from django.urls import path
from . import views

urlpatterns = [
    path('calorieCounter/', views.calorieCounter, name='calorieCounter'),
    path('', views.homepage, name='homepage'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout')
]

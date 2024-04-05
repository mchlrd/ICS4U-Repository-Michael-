from django.contrib import admin
from django.urls import path
from .views import home,signin,signup,signout, valid, predict

urlpatterns = [
    path('', home, name='home'),
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('signout', signout, name='signout'),
    path('valid', valid, name='valid'),
    path('predict', predict, name='predict'),
]
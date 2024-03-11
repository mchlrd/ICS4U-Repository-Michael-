from django.contrib import admin
from django.urls import path
from .views import home,signin,signup,signout

urlpatterns = [
    path('', home, name='home'),
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('signout', signout, name='signout')
]
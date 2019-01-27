from django.urls import path
from .views import home
from .views import logoutUser

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logoutUser, name='logout'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('removebg', views.removebg, name='removebg'),

]
from django.urls import path
from . import views

from django.contrib import admin
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #/generate/
    path('', views.index, name='index'),

    #/generate/details
    path('<int:pizza_id>/',  views.detail, name='detail'),

    #/generate/details
    path('nutrition',  views.nutrition, name='nutrition'),

    #/generate/form
    path('form',  views.form, name='form'),

    path('AllPizza/', views.getAllPizza, name='AllPizza'),
    path('Pizza/<int:id>/', views.getPizza, name='Pizza'),
    path('CreatePizza/', views.createPizza, name='CreatePizza'),


    #/generate/integration
    path('integration', views.integration, name='integration')


]

from django.urls import path, include
from . import views

from django.contrib import admin
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #/generate/
    path('index/', views.index, name='index'),

    #/generate/details
    path('<int:pizza_id>/',  views.detail, name='detail'),

    #/generate/details
    path('nutrition',  views.nutrition, name='nutrition'),

    #/generate/form
    path('form',  views.form, name='form'),

    #/generate/integration
    path('', views.integration, name='integration'),
    path('external/', views.external, name='externel'),
    path('piecemeal/', views.piecemeal, name='piecemeal')

]

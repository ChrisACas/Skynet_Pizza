from django.urls import path
from . import views

urlpatterns = [
    #/generate/
    path('', views.index, name='index'),

    #/generate/details
    path('<int:pizza_id>/',  views.detail, name='detail'),

    #/generate/details
    path('nutrition',  views.nutrition, name='nutrition'),


]

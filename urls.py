from django.contrib import admin
from django.urls import path
from . import views
from demoapp.views import *
urlpatterns = [
    
    #django CRUD
    path('create_data', views.create_data, name= 'create_data'),
    path('retrieve', views.retrieve, name = 'retrieve'),
    path('update1/<int:id>', views.update1, name = 'update1'),
    path('delete1/<int:id>', views.delete1, name = 'delete1'),

    
]

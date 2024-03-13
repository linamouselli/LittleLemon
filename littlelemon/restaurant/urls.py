from django.contrib import admin 
from django.urls import path, include
from . import views
from rest_framework import routers, viewsets
  
urlpatterns = [ 
    #path('', views.sayHello, name='sayHello'), 
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    #path('booking/', bookingview.as_view()),
]
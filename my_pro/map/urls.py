from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.map, name='map'),
    path('map2/',views.map2, name='map2' ),
]
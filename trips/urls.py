from django.urls import path
from . import views
urlpatterns=[
    path('',views.trips,name='trips'),
    path('<slug:catogery_slug>/',views.trips,name='places_by_catogery'),
]
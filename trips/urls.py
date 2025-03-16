from django.urls import path
from . import views
urlpatterns=[
    path('',views.trips,name='trips'),
    path('catogery/<slug:catogery_slug>/',views.trips,name='places_by_catogery'),
    path('catogery/<slug:catogery_slug>/<slug:place_slug>/',views.place_details,name='place_details'),
    path('search/',views.search,name='search')
]
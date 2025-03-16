from django.shortcuts import render,get_object_or_404
from .models import Places
from catogery.models import Catogery
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.
def trips(request,catogery_slug=None):
    catogeries=None
    places=None
    
    if catogery_slug != None:
        catogeries=get_object_or_404(Catogery,slug=catogery_slug)
        places=Places.objects.filter(catogery=catogeries,allowed=True)
        places_count=places.count()
    
    else:
        places=Places.objects.all().filter()
        places_count=places.count()
        
        
  
    context={
        'places':places,
        'places_count':places_count
        

    }
    return render(request,'trips/trips.html',context)

def place_details(request,catogery_slug,place_slug):
    try:
        single_place=Places.objects.get(catogery__slug=catogery_slug,slug=place_slug)
    except Exception as e:
        raise e
    context={
        'single_place':single_place
    }

    return render(request,'trips/place_details.html',context)

def search(request):
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            places=Places.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(place_name__icontains=keyword))
            places_count=places.count()
    context={
        'places':places,
        'places_count':places_count
        

    }
    return render(request,'trips/trips.html',context)
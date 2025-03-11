from django.shortcuts import render,get_object_or_404
from .models import Places
from catogery.models import Catogery
# Create your views here.
def trips(request,catogery_slug=None):
    catogeries=None
    places=None
    if catogery_slug != None:
        catogeries=get_object_or_404(Catogery,slug=catogery_slug)
        places=Places.objects.filter(catogery=catogeries,allowed=True)
    
    else:
        places=Places.objects.all().filter(allowed=True)
  
    context={
        'places':places,
    }
    return render(request,'trips/trips.html',context)
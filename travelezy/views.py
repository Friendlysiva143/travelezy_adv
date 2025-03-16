from django.shortcuts import render
from trips.models import Places
def home(request):
    places=Places.objects.all().filter(allowed=True)
    context={
        'places':places,
    }
    return render(request,'index.html',context)
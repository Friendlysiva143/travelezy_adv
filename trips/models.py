from django.db import models
from catogery.models import Catogery
from django.urls import reverse

# Create your models here.
class Places(models.Model):
    place_name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=200,blank=True)
    start_date=models.DateField()
    end_date=models.DateField()
    images=models.ImageField(upload_to='photos/places')
    allowed=models.BooleanField(default=True)
    catogery=models.ForeignKey(Catogery,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now_add=True)
    def get_url(self):
        return reverse('place_details',args=[self.catogery.slug,self.slug])
    class Meta:
        verbose_name='place'
        verbose_name_plural='places'
    def __str__(self):
        return self.place_name



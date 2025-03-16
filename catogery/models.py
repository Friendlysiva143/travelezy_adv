from django.db import models
from django.urls import reverse
# Create your models here.
class Catogery(models.Model):
    catogery_name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    desc=models.TextField(max_length=200,blank=True)
    cat_img=models.ImageField(upload_to='photos/catogeries',blank=True)
    class Meta:
        verbose_name='catogery'
        verbose_name_plural='catogeries'
        
    def get_url(self):
        return reverse('places_by_catogery',args=[self.slug])
    def __str__(self):
        return self.catogery_name
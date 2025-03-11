from django.contrib import admin
from .models import Places

# Register your models here.
class PlaceAdmin(admin.ModelAdmin):
    list_display=('place_name','start_date','end_date','catogery','allowed')
    prepopulated_fields={'slug':('place_name',)}
admin.site.register(Places,PlaceAdmin)
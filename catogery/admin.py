from django.contrib import admin
from .models import Catogery
# Register your models here.
class CatogeryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('catogery_name',)}
    list_display=('catogery_name','slug')
admin.site.register(Catogery,CatogeryAdmin)


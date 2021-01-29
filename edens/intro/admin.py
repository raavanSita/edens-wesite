from django.contrib import admin
from .models import newArrivals , offers
# Register your models here.

class newArrivalsAdmin(admin.ModelAdmin):
    list_display=('title','discription','price','img_url')
class offersAdmin(admin.ModelAdmin):
    list_display=('title','price','img_url')


admin.site.register(newArrivals,newArrivalsAdmin)
admin.site.register(offers,offersAdmin)
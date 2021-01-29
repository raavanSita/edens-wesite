from django.shortcuts import render
from .models import newArrivals ,offers
# Create your views here.
def index(request):
    newArrivals_object = newArrivals.objects.all()
    offers_object = offers.objects.all()
    cont = {
        'newArrivals_object':newArrivals_object,
        'offers_object':offers_object }
    return render(request,'index.html',cont)


    
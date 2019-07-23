from django.shortcuts import render
from django.http import HttpResponse
from realtors.models import Realtor
from listings.models import Listing
from listings.choices import bedroom_choices,price_choices,state_choices
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    listings = Listing.objects.all()[:3]
    context = {
        'listings':listings,
        'state_choice': state_choices,
        'bedroom_choice': bedroom_choices,
        'price_choice': price_choices
    }
    return render(request,'pages/index.htm',context)

def about(request):
    realtors = Realtor.objects.all()
    
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors' : realtors,
        'mvp_realtors': mvp_realtors
    }
    
    return render(request,'pages/about.htm',context)
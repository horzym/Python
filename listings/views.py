from django.shortcuts import render

def index(request):
     return render(request,'listings/listings.htm')
def listing(request):
    return render(request,'listings/listing.htm')
def search(request):
    return render(request,'listings/search.htm')
# Create your views here.

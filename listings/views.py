from django.shortcuts import get_object_or_404, render
from listings.models import Listing
from realtors.models import Realtor
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from listings.choices import bedroom_choices,price_choices,state_choices
def index(request):
     listings = Listing.objects.order_by('-list_date').filter(is_published=True)
     paginator = Paginator(listings,6)
     page = request.GET.get('page')
     paged_listings=paginator.get_page(page)
    
     context = {
          'listings': paged_listings
     }

     return render(request,'listings/listings.htm', context)

def listing(request,listing_id):
     listing = get_object_or_404(Listing,pk=listing_id)
     #realtor = Realtor.objects.all().filter(realtor)
     context={
          'listing':listing
     }

     return render(request,'listings/listing.htm',context)

def search(request):
     listing_query= Listing.objects.all()
#keywords
     if 'keywords' in request.GET:
          keywords=request.GET['keywords']
          if keywords:
             listing_query = listing_query.filter(description__icontains=keywords)
#city search
     if 'city' in request.GET:
          city=request.GET['city']
          if city:
             listing_query = listing_query.filter(city__iexact=city)
#state search
     if 'state' in request.GET:
          print(request.GET)
          state=request.GET['state']
          if state:
               listing_query=listing_query.filter(state__iexact=state)
#bedrooms search
     if 'bedrooms' in request.GET:
          print(request.GET)
          bedrooms=request.GET['bedrooms']
          if bedrooms:
               listing_query=listing_query.filter(bedrooms__gte=bedrooms)
#price search
     if 'price' in request.GET:
          print(request.GET)
          price=request.GET['price']
          if price:
               listing_query=listing_query.filter(price__lte=price)
     context={
          'listings':listing_query,
          'state_choice': state_choices,
          'bedroom_choice': bedroom_choices,
          'price_choice': price_choices,
          'values': request.GET
     }
     return render(request,'listings/search.htm',context)
# Create your views here.

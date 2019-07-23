from django.contrib import admin
from listings.models import Listing
from realtors.models import Realtor

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display=('id','title','is_published','price','realtor','list_date')
    list_display_links=('id','title')
    list_editable=('realtor','price','is_published')
    search_fields=('title','price',)

admin.site.register(Listing,ListingAdmin)
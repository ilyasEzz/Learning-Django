from django.shortcuts import render, get_object_or_404
from .models import Listings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    # order_by(-variable): - means descendent
    listing_view = Listings.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listing_view, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {'listings': paged_listings}
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    # get_object_or_404: Returns the object matching the given lookup parameters, like the "get()" method 
    # ( "pk": primary key ): given as a parameter of path() in urls.py '<int:listing_id>'
    # but it raises Http404 instead of the model’s DoesNotExist exception
    listing = get_object_or_404(Listings, pk=listing_id)
    
    context = {
        'listing': listing
    }   
    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')

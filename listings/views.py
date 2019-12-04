from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .choices import bedroom_choices, price_choices
from .models import Listings
from contacts.forms import UserCommentForm, GuestCommentForm


# Create your views here.


def index(request):
    # order_by(-variable): - means descendent
    listing_view = Listings.objects.order_by(
        '-list_date').filter(is_published=True)

    paginator = Paginator(listing_view, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': listing_view,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    # get_object_or_404: Returns the object matching the given lookup parameters, like the "get()" method
    # ( "pk": primary key ): given as a parameter of path() in urls.py '<int:listing_id>'
    # but it raises Http404 instead of the model’s DoesNotExist exception
    listing = get_object_or_404(Listings, pk=listing_id)

    if request.user.is_authenticated:
        form = UserCommentForm(request.POST or None)
    else:
        form = GuestCommentForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.instance.listings = listing
            form.save()

    context = {
        'listing': listing,
        'form': form
    }
    return render(request, 'listings/listing.html', context)


def search(request):
     # https://docs.djangoproject.com/en/2.2/topics/db/search/
    queryset_listings = Listings.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_listings = queryset_listings.filter(
                description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            # query
            queryset_listings = queryset_listings.filter(city__iexact=city)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            # lte == less than or exact
            queryset_listings = queryset_listings.filter(
                bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            # lte == less than or exact
            queryset_listings = queryset_listings.filter(price__lte=price)

    context = {
        'listings': queryset_listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)

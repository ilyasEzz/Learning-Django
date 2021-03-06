from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listings
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices


def index(request):
    listing_view = Listings.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listing_view,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.all()
    mvp_realtor = realtors.filter(is_mvp=True)
    context = {'realtors': realtors, 'mvp_realtor': mvp_realtor}
    return render(request, 'pages/about.html', context)

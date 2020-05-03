from django.shortcuts import render

from listings.models import Listing
from realtors.models import Realtror
from listings.choices import state_choices, price_choices, bedroom_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices
    }


    return render(request, 'pages/index.html', context)

def about(request):
    #Get all realtors
    realtors = Realtror.objects.order_by('-hire_date')

    #Get MVP
    mvp_realtors = Realtror.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)
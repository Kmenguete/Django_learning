from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Title


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})


def band_detail(request, band_id):
    return render(request, 'listings/band_detail.html', {'id': band_id})


def about(request):
    return render(request, 'listings/about.html')


def listings(request):
    titles = Title.objects.all()
    return render(request, 'listings/listings.html', {'titles': titles})


def contact(request):
    return render(request, 'listings/contact.html')

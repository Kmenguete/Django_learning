from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Title
from listings.forms import ContactUsForm


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {'band': band})


def about(request):
    return render(request, 'listings/about.html')


def listings(request):
    titles = Title.objects.all()
    return render(request, 'listings/listings.html', {'titles': titles})


def listing_detail(request, id):
    title = Title.objects.get(id=id)
    return render(request, 'listings/listing_detail.html', {'title': title})


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
    else:
        form = ContactUsForm()

    return render(request, 'listings/contact.html', {'form': form})

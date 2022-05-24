from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Title
from listings.forms import ListingForm, BandForm, ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect


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
        if form.is_valid():
            send_mail(subject=f'Message from {form.cleaned_data["name"] or "unnamed"} via Merchex Contact Us form',
                      message=form.cleaned_data['message'],
                      from_email=form.cleaned_data['email'],
                      recipient_list=['admin@merchex.xyz'],
                      )
            return redirect('email-sent')
    else:
        form = ContactUsForm()

    return render(request, 'listings/contact.html', {'form': form})


def email_sent(request):
    return render(request, 'listings/email_sent.html')


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()

    return render(request, 'listings/band_create.html', {'form': form})


def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_update.html', {'form': form})


def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            title = form.save()
            return redirect('listing-detail', title.id)
    else:
        form = ListingForm()
    return render(request, 'listings/listing_create.html', {'form': form})


def listing_update(request, id):
    title = Title.objects.get(id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=title)
        if form.is_valid():
            form.save()
            return redirect('listing-detail', title.id)
    else:
        form = ListingForm(instance=title)
    return render(request, 'listings/listing_update.html', {'form': form})

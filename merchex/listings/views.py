from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Title


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})


def about(request):
    return HttpResponse("<h1>About us</h1> <p>We love merchex !</p>")


def listings(request):
    titles = Title.objects.all()
    return render(request, 'listings/listings.html', {'titles': titles})


def contact(request):
    return HttpResponse("<h1>Contact us</h1> <p>Contact information.....</p>")

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("<h1>Voici ma première page web écrit avec Django</h1>")


def about(request):
    return HttpResponse("<h1>About us</h1> <p>We love merchex !</p>")


def listings(request):
    return HttpResponse("<h1>A list items</h1> <p>The list items</p>")


def contact(request):
    return HttpResponse("<h1>Contact us</h1> <p>Contact information.....</p>")

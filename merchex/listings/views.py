from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p> My favorite bands are: </p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
""")


def about(request):
    return HttpResponse("<h1>About us</h1> <p>We love merchex !</p>")


def listings(request):
    return HttpResponse("<h1>A list items</h1> <p>The list items</p>")


def contact(request):
    return HttpResponse("<h1>Contact us</h1> <p>Contact information.....</p>")

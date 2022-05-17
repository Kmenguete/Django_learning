from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Title


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
    titles = Title.objects.all()
    return HttpResponse(f"""
        <h1>A titles list</h1> 
        <p>Here are my favorite titles: </p>
        <ul>
            <li>{titles[0].title}</li>
            <li>{titles[1].title}</li>
            <li>{titles[2].title}</li>
        </ul>
""")


def contact(request):
    return HttpResponse("<h1>Contact us</h1> <p>Contact information.....</p>")

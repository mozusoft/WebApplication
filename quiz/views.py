
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.utils import timezone


def subject(request):
    # return HttpResponse('<h1 style = "color: red" > Hello Olimjon</h1>')
    return render(request, 'base.html', context={'name': 'olimjon', 'time': timezone.now()})

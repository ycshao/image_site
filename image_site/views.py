from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hello(request):
    print(request)
    return HttpResponse("Hello World!")

def home(request):
    return HttpResponse("This is home.")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt})

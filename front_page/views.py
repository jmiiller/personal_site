from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'front_page/front_page.html', {})

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    request.session['random_word'] = get_random_string(length=14)
    if "counter" not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1
    return render(request, 'wordgen_app/index.html')

def random_word(request):
    return redirect ('/')

def reset(request):
    request.session['counter'] = 0
    return redirect ('/')
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from test_ajax.models import User
import time

def test_ajax(request):
    return render(request, 'test_ajax/test_ajax.html')

def create_user (request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password =request.POST['password']

        User.objects.create(
            name = name,
            email = email,
            password = password
        )

        return HttpResponse('')
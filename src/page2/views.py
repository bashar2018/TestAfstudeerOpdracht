from django.shortcuts import render

# Create your views here.

def page2(request):
    return render(request, 'page2/page2.html')

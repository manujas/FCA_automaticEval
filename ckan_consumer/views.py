from django.shortcuts import render

def index(request):
    return render(request, 'ckan_consumer/index.html')

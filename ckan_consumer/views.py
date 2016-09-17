from django.shortcuts import render

def index(request):
    query = None
    if request.method == 'GET' and 'q' in request.GET:
        query = request.GET['q']

    return render(request, 'ckan_consumer/index.html', {'query': query})

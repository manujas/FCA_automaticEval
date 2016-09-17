from django.shortcuts import render
from ckan_consumer import ckan_search

def index(request):
    data = None
    if request.method == 'GET' and 'q' in request.GET:
        query = request.GET['q']

        url = 'http://www.datos.gob.ar/'
        data = ckan_search.package_search(url, query, 10)

    return render(request, 'web/index.html', {'data': data})

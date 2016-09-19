from django.shortcuts import render
from django.contrib import messages
from ckan_consumer import ckan_search

def index(request):
    data = None
    query = None

    if request.method == 'GET' and 'q' in request.GET:
        query = request.GET['q']

        url = 'http://www.datos.gob.ar/'

        try:
            data = ckan_search.package_search(url, query, 10)
        except Exception as e:
            messages.error(request, 'Algo sucedio mal, vuelve a intentarlo.')

        return render(request, 'web/index.html', {'data': data, 'query': query})

    return render(request, 'web/index.html')

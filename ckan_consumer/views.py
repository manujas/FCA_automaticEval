from django.shortcuts import render
from ckanapi import RemoteCKAN

def index(request):
    data = None
    if request.method == 'GET' and 'q' in request.GET:
        query = request.GET['q']

        ckan = RemoteCKAN('http://www.datos.gob.ar/')
        search_params = {
            'q': query,
            'rows': 10,

        }
        data = ckan.call_action('package_search', data_dict=search_params)

    return render(request, 'ckan_consumer/index.html', {'data': data})

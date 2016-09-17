from ckanapi import RemoteCKAN

def package_search(site, query, rows):
    ckan = RemoteCKAN(site)
    search_params = {
        'q': query,
        'rows': rows,
    }
    results = ckan.call_action('package_search', data_dict=search_params)

    return results

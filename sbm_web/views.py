from django.http import HttpResponse
from django.template import loader

def page_index(request):

    template = loader.get_template('web/index.html')
    return HttpResponse(template.render(request=request))

def montre_homme(request):

    tpwatch = loader.get_template('web/watch_men.html')
    return HttpResponse(tpwatch.render(request=request))
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from homepage.models import Letter
# models

# Create your views here.
def home(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def ajax(request):
    homedata = Letter.objects.all().values()
    return JsonResponse(list(homedata), safe=False)

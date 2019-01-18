from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from homepage.models import Letter
from homepage.models import Category
# models

# Create your views here.
def home(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def ajax(request):
    request_cat = request.GET['q'].lower()
    cat = Category.objects.get(slug=request_cat)
    print(cat)
    homedata = Letter.objects.filter(category=cat).values()
    return JsonResponse(list(homedata), safe=False)

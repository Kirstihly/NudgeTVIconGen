'''
    If you meet any problems,
    please contact
    Leying Hu
    hu.leying@columbia.edu
'''
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .forms import *

from .models import Urls

def index(request):
    latest_urls_list = Urls.objects.order_by('-pub_date')[:50]
    template = loader.get_template('URLShortener/index.html')
    context = {'latest_urls_list': latest_urls_list}
    return HttpResponse(template.render(context, request))

def detail(request, urls_id):
    try:
        to_url = Urls.objects.get(pk=urls_id)
    except Urls.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'URLShortener/detail.html', {'to_url':to_url})

def icon_image_view(request):
    
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'icon_image_form.html', {'form' : form})


def success(request):
    return HttpResponse('successfuly uploaded')

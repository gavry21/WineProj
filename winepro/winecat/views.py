from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from .models import Wine
from .models import Label
from .models import Sort
from .models import Comment
from .forms import WineForm
from django.core.context_processors import csrf

def home(request):
    home = 'Home page test'
    return render_to_response('home.html',{'name':home})

def cat_detail(request, id = None):
    instance=get_object_or_404(Wine,id=id)
    context={'country':'Wine Detail',
    'instance':instance}
    return render(request,'cat_detail.html',context)

def cat_create(request):
    form=WineForm()
    if request.method=='POST':
        form=WineForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
    context = {
        'page_title':'Create',
        'form':form
    }
    return render(request,'cat_create.html',context)

def cat_update(request,id=None):
    instance=get_object_or_404(Wine,id=id)
    form=WineForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
    context={
        'page_title':'Update',
        'country':instance.country,
        'instance':instance,
        'form':form
    }
    return render(request,'cat_create.html', context)

def cat_delete(request):
    return HttpResponse('<h1>Delete</h1>')  

def cat_list(request):
    queryset = Wine.objects.all()
    context = {'queryset':queryset,'country':'Wine Catalog'}
    return render(request,'index.html', context)
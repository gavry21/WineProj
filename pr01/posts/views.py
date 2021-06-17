from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from .models import Post
from .models import Author
from .models import Comment
from .forms import PostForm
from django.core.context_processors import csrf

def post_home(request):
    home = 'Home page test'
    return render_to_response('home.html',{'name':home})

def post_detail(request, id = None):
    instance=get_object_or_404(Post,id=id)
    context={'title':'Post Detail',
    'instance':instance}
    return render(request,'post_detail.html',context)

def post_create(request):
    form=PostForm()
    if request.method=='POST':
        form=PostForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
    context = {
        'page_title':'Create',
        'form':form
    }
    return render(request,'post_create.html',context)

def post_update(request,id=None):
    instance=get_object_or_404(Post,id=id)
    form=PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
    context={
        'page_title':'Update',
        'title':instance.title,
        'instance':instance,
        'form':form
    }
    return render(request,'post_create.html', context)

def post_delete(request):
    return HttpResponse('<h1>Delete</h1>')  

def post_list(request):
    queryset = Post.objects.all()
    context = {'queryset':queryset,'title':'Post List'}
    return render(request,'index.html', context)
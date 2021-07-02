from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import BlogForm
# Create your views here.
#all get order_by filter exclude
def home(request):
    blogs = Blog.objects.order_by('-date')
    search = request.GET.get('search')
    if search == 'true':
        author = request.GET.get('writer')
        blogs = Blog.objects.filter(writer=author).order_by('-date') #반대는 exclude
        return render(request, 'home.html', {'blogs':blogs})
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs})

def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'htmlform':form})

def detail(request, idid):
    oneblog = get_object_or_404(Blog, id=idid)
    return render(request, 'detail.html', {'b':oneblog})

def create(request):
    form = BlogForm(request.POST,request.FILES)
    if form.is_valid():
        nblog = form.save(commit=False)
        nblog.date = timezone.now()
        nblog.save()
        return redirect('urldetail', nblog.id)

    return redirect('urlhome')
    
     

def edit(request, idid):
    eblog = Blog.objects.get(id = idid)
    return render(request, 'edit.html', {'c': eblog})

def update(request, idid):
    ublog = Blog.objects.get(id = idid)
    ublog.title = request.POST['utitle']
    ublog.writer = request.POST['uwriter']
    ublog.body = request. POST['ubody']
    ublog.image = request.FILES.get('uimage')
    ublog.date = timezone.now()
    ublog.save()
    return redirect('urldetail', ublog.id)

def delete(request, idid):
    dblog = Blog.objects.get(id = idid)
    dblog.delete()
    return redirect('urlhome')


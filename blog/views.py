from django.shortcuts import render,get_object_or_404
from .models import Blog

def blog_all(request):
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request,'blog/blog_all.html',{'blogs':blogs})

def details(request, blog_id):
    blog  = get_object_or_404(Blog, pk=blog_id)
    return render(request,'blog/details.html',{'blog':blog})

# Create your views here.

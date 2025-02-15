from django.shortcuts import render, get_object_or_404
from myapp.models import Blog

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'myapp/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'myapp/blog_detail.html', {'blog': blog})

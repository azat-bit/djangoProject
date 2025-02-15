from django.shortcuts import render, get_object_or_404
from myapp.models import Tag, Blog

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'myapp/tag_list.html', {'tags': tags})

def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    blogs = Blog.objects.filter(tags=tag)
    return render(request, 'myapp/tag_detail.html', {'tag': tag, 'blogs': blogs})

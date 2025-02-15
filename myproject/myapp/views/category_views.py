from django.shortcuts import render, get_object_or_404
from myapp.models import Category, Blog

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'myapp/category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    blogs = Blog.objects.filter(category=category)
    return render(request, 'myapp/category_detail.html', {'category': category, 'blogs': blogs})

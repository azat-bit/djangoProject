from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from myapp.models import Blog, Category

# Blogları Listeleme
def blog_list(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()  # Blog eklerken kategori seçebilmek için
    return render(request, 'myapp/blog_list.html', {'blogs': blogs, 'categories': categories})

# Blog Detay Sayfası
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'myapp/blog_detail.html', {'blog': blog})

# Blog Ekleme (AJAX ile Sayfa Yenilenmeden)
@login_required
def blog_create_ajax(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        category_id = request.POST.get("category")
        
        # Kategori kontrolü
        category = get_object_or_404(Category, id=category_id)

        # Blog oluştur
        blog = Blog.objects.create(
            title=title,
            content=content,
            category=category,
            author=request.user
        )

        # JSON ile yeni eklenen blogu dön
        return JsonResponse({
            "success": True,
            "id": blog.id,
            "title": blog.title,
            "content": blog.content[:100] + "...",  # İlk 100 karakter
            "author": blog.author.username,
            "category": blog.category.name
        })
    
    return JsonResponse({"success": False}, status=400)

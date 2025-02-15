from django.shortcuts import render, get_object_or_404
from myapp.models import Blog, Comment

def comment_list(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comments = blog.comments.all()
    return render(request, 'myapp/comment_list.html', {'blog': blog, 'comments': comments})

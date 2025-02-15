"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import blog_list, blog_detail, comment_list, category_list, category_detail, tag_list, tag_detail, user_profile
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_list, name='blog_list'),
    path('blog/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('blog/<int:blog_id>/comments/', comment_list, name='comment_list'),
    path('categories/', category_list, name='category_list'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('tags/', tag_list, name='tag_list'),
    path('tag/<int:tag_id>/', tag_detail, name='tag_detail'),
    path('user/<int:user_id>/', user_profile, name='user_profile'),
        path('login/', LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='blog_list'), name='logout'),

]

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog_list')  # Giriş sonrası yönlendirme
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Kullanıcı adı kontrolü
        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu kullanıcı adı zaten alınmış.")
            return redirect('register')

        # E-posta kontrolü
        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu e-posta adresi zaten kullanılıyor.")
            return redirect('register')

        # Şifre doğrulama
        if password1 != password2:
            messages.error(request, "Şifreler eşleşmiyor.")
            return redirect('register')

        # Kullanıcıyı kaydet
        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        messages.success(request, "Kayıt işlemi başarılı!")
        return redirect('blog_list')

    return render(request, 'myapp/register.html')


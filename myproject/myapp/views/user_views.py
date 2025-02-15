from django.shortcuts import render, get_object_or_404
from myapp.models import UserProfile
from django.contrib.auth.models import User

def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(UserProfile, user=user)
    return render(request, 'myapp/user_profile.html', {'user': user, 'profile': profile})

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import UserProfile

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        nickname = request.POST.get('nickname')
        user = User.objects.create_user(username=username, password=password)
        UserProfile.objects.create(user=user, nickname=nickname)
        return JsonResponse({'status': 'User registered successfully'})
    return JsonResponse({'status': 'Invalid request'})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'Login successful'})
        return JsonResponse({'status': 'Invalid credentials'})
    return JsonResponse({'status': 'Invalid request'})

def find_user_by_nickname(request):
    if request.method == 'GET':
        nickname = request.GET.get('nickname')
        try:
            user_profile = UserProfile.objects.get(nickname=nickname)
            return JsonResponse({'username': user_profile.user.username, 'nickname': user_profile.nickname})
        except UserProfile.DoesNotExist:
            return JsonResponse({'status': 'User not found'})
    return JsonResponse({'status': 'Invalid request'})

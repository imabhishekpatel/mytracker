# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from userLogin.forms.loginForm import *

class CustomTokenObtainPairView(TokenObtainPairView):
    pass  # You can customize this view if needed

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                return redirect('/checkInCheckOut/check_in_out/')  # Redirect to homepage after login
    else:
        form = LoginForm()
    return render(request, 'userLogin/login.html', {'form': form})

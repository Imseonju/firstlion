from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username = username, password = password)
            if user is not None:
                login(request, user)
        return redirect('urlhome')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'a':form})

def logout_view(request):
    logout(request)
    return redirect('urlhome')

def signup_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user)
        return redirect('urlhome')
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'b':form})
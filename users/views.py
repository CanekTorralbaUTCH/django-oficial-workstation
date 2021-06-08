from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#Views
from django.views import View

#Models
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    """ Login View """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('landing')
        else:
            try:
                user = User.objects.get(username=username)
                return render(request, 'users/login.html',{'error':'Invalid password'})
            except:
                return render(request, 'users/login.html',{'error':'Invalid username and password'})

    
    
    return render(request, 'users/login.html')

def signup(request):
    return render(request, 'users/signup.html')

@login_required
def landing(request):
    return render(request,'landing.html')

@login_required
def logout_view(request):
    """ Logout an user view """
    logout(request)
    return redirect('login')
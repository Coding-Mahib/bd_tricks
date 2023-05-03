from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from app.config import SITE

# Create your views here.

def home(req):
    return

def login_(req):
    if req.method == 'POST':
        form = AuthenticationForm(req, data=req.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(req, user)
                messages.info(req, f'You are logined in as {username}')
            else:
                messages.error(req,"Invalid username or password.")
        else:
            messages.error(req,"Invalid username or password.")
       
    form = AuthenticationForm()

    return render(req, 'login.html', context={'login_form': form, 'SITE': SITE, 'type': type})
def logout_(req):
    logout(req)
    messages.info(req, "You are successfully logged out.")

    return redirect('login')

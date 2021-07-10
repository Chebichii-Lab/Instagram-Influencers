from gram.forms import SignupForm
from django.http import request

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
       
    return render(request,"home.html")


#Sign up Function
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'registration/registration_form.html', {'form': form})


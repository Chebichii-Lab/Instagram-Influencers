from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')


@login_required(login_url='/accounts/register/')
def home(request):
       
    return render(request,"home.html")

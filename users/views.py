from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")
    


#login
def login_view(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users"))
        else:
            return render(request, 'users/login.html',{
                "message": "Invalid credentials"
            })
    return render(request, "users/login.html")

#logout
def logout_view(request):
    # return render(request, "user/logout.html")
    logout(request)
    return render(request, "users/login.html",{
        "message": "Successfully logged out."
    })
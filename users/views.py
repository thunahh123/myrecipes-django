from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.forms import UserRegistrationForm
from users.models import CustomUser

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

#signup new account
def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
            )
            return HttpResponseRedirect(reverse("users"))  # Redirect to a login page or home page
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", {'form': form})

#register
# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return HttpResponseRedirect("users")  
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'register.html', {'form': form})

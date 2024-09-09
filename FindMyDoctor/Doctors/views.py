from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth



# Create your views here.


def Member(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Login"))
    return render(request, "Doctors/profile.html")
    

def Login(request):
    if request.method == "POST":
        username= request.POST["username"]
        password= request.POST["password"]
        user= authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            return render(request, "Doctors/profile.html")
        
        else:
            return render(request, "Doctors/Login.html", {
                "message": "invalid credentials"
            })

    return render(request, "Doctors/Login.html")

def Logout(request):
    logout(request)
    return render(request, "Doctors/Login.html",{
        "message": " You have been logged out"
    })


def Signup(request):
    if request.method == "POST":
        first_name= request.POST["first_name"]
        last_name= request.POST["last_name"]
        email= request.POST["email"]
        username= request.POST["username"]
        password1= request.POST["password1"]
        password2= request.POST["password2"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, "Doctors/Signup.html", {
                "message": "Username taken"
                })

            elif User.objects.filter(email=email).exists():
                return render(request, "Doctors/Signup.html", {
                "message": "email already used"
                })
        
            else:    
                user= User.objects.create_user(username=username, password= password1,
                                                email= email, first_name=first_name, last_name=last_name)
                user.save()
        else:
            return render(request, "Doctors/Signup.html", {
                "message": "passwords don't match"
            })


        return render(request, "Doctors/Login.html")
    else:
        return render(request, "Doctors/Signup.html")
    
def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse(Login))
    return render(request, 'Doctors/profile.html')
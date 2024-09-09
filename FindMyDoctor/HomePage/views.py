from django.shortcuts import render, get_object_or_404
from Doctors.models import Doctors
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
# Create your views here.

def Home(request):
    login_flag= request.user.is_authenticated
    selected_adress = request.GET.get('Adress', '')
    selected_specialization = request.GET.get('Specialization', '')

    doc_list = Doctors.objects.filter(
            Adress__icontains=selected_adress,
            Specialization__icontains=selected_specialization
        )
    
    context = {
        "doctors": doc_list,
        'login_flag': login_flag,
    }

    
    return render(request, "HomePage/Home.html", context)



def Details_Page(request, id):
    doctor = get_object_or_404(Doctors, id=id)
    
    return render(request, "HomePage/Details.html", {"doctor": doctor})
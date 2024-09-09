from django.urls import path
from . import views

urlpatterns = [
    path("Member/" , views.Member, name="MyDoctorMember"),
    path("Login/", views.Login, name="MyDoctorLogin"),
    path("Logout/", views.Logout, name="MyDoctorLogout"),
    path("Signup/", views.Signup, name="MyDoctorSignup"),
    path("Profile/", views.profile, name="MyDoctorProfile")
]

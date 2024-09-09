from django.urls import path
from . import views

urlpatterns = [
    path("Home", views.Home, name="MyDoctorHome"),
    path('doctor/<int:id>/', views.Details_Page, name="MyDoctorDetails")
]

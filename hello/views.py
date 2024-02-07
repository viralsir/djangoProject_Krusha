from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse("<h1>Hello</h1>");

def Aboutus(request):
    return HttpResponse("<h1 style='color:red'>About Us </h1>")

def Contactus(request):
    return HttpResponse("<h1>Contact Us </h1>")


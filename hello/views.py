from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request,name):
  #  return HttpResponse("<h1>Hello</h1>");
  return render(request,"hello/home.html",{"username":name})

def Aboutus(request):
   return render(request,"hello/Aboutus.html")

def Contactus(request):
    #return HttpResponse("<h1>Contact Us </h1>")
  return render(request,"hello/ContactUs.html")


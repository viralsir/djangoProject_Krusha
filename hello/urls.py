from django.urls import path
from .views import *

urlpatterns=[
    path('home/', Home, name="hello-home"),
    path("about/", Aboutus, name="hello-aboutus"),
    path("contactus/", Contactus, name="hello-contactus")

]
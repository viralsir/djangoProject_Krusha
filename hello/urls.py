from django.urls import path
from .views import *

urlpatterns=[
    path('home/<str:name>', Home, name="hello-home"),
    path("about/", Aboutus, name="hello-aboutus"),
    path("contactus/", Contactus, name="hello-contactus")

]
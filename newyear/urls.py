from django.urls import path
from .views import home,employeeview
urlpatterns=[
    path("",home,name="newyear-home"),
    path("employees/",employeeview,name="employee-view")
]


from django.shortcuts import render
from datetime import  datetime

employees=[
    {"id":1,"name":"vimal","salary":23000},
    {"id":2,"name":"viren","salary":43000},
    {"id":3,"name":"vijay","salary":53000},
    {"id":4,"name":"vipul","salary":33000},

]


# Create your views here.
def home(request):
    date=datetime.utcnow()
    return render(request,"newyear/home.html",{
        "month":date.month,
        "day":date.day
    })

#  functionname : employeeview
#  description: this function will send employee list into template called employeelist.html for
#   viewing employee record
#  return type : render
#  parameter : request

def employeeview(request):
    return render(request,"newyear/employee_list.html",{
        "employeelist":employees
    })
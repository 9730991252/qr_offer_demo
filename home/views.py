from django.shortcuts import render, redirect
from owner.models  import *
from django.contrib import messages
# Create your views here.

def index(request):
    return render (request, 'home/index.html')


def customer_scan(request, tag_number):
    print(tag_number)
    context={
        'tag_number':tag_number
    }
    return render(request,'customer/customer_scan.html', context)



def login(request):
    if request.session.has_key('office_mobile'):
        return redirect('office_home')
    else:
        if request.method == "POST":
            number=request.POST ['number']
            pin=request.POST ['pin']
            e= Office_employee.objects.filter(mobile=number,pin=pin,status=1)
            if e:
                request.session['office_mobile'] = request.POST["number"]
                return redirect('office_home')
            else:
                messages.success(request,"please insert correct information or call more suport 9730991252")            
                return redirect('login')
    return render(request, 'home/login.html')


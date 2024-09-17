from django.shortcuts import render, redirect
from owner.models  import *
from django.contrib import messages
import random
import string
# Create your views here.
#***************************************

#***************************************



def index(request):
    return render (request, 'home/index.html')

def test(request):
    return render (request, 'home/test.html')

def customer_scan(request, tag_number):
    if Qr_code.objects.filter(tag_number=tag_number).exists():
        qr = Qr_code.objects.get(tag_number=tag_number)
        if qr.scan_status == 0:
            a = ["apple", "banana", "cherry"]
            award = random.choice(a)
            item_id = reward_item_save(award)
            Customer_reward(
                reward_item_id = item_id,
                qr_code_id = qr.id
            ).save()
            qr.scan_status = 1
            qr.save()
            return redirect(f'/customer_scan/{tag_number}')
        if qr.scan_status == 1:
            c_r = Customer_reward.objects.filter(qr_code_id=qr.id).first()
        context={
            'tag_number':tag_number,
            's':Shop.objects.get(status=1),
            'c_r':c_r
        }
        return render(request,'customer/customer_scan.html', context)  
    else:
        return redirect('/')

def reward_item_save(item_name):
    if Reward_item.objects.filter(name=item_name).exists():
        r = Reward_item.objects.get(name=item_name)
        return r.id
    else:
        Reward_item(
            name=item_name
        ).save()
        r = Reward_item.objects.get(name=item_name)
        return r.id



























































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


from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import *
from owner.models import *
import random
import datetime 
import string 
# Create your views here.

def generate_tag(request):
    if request.method == 'GET':
        tag_qty = request.GET['qty']
        eid = request.GET['eid']
        qr = Qr_code.objects.all().count()
        qr += 1
        for i in range (int(tag_qty)):
            code = f"{random.choice(string.ascii_letters)}{random.choice(string.ascii_letters)}-{qr}{random.randint(1,10000)}"
            Qr_code(
                employee_id=eid,
                tag_number=code, 
                sr_num=qr
                ).save() 
            qr += 1
        tag = Qr_code.objects.filter().order_by('-id')[0:int(tag_qty)]
        context2={
            'tag_list':Qr_code.objects.filter().order_by('-id')[0:1000]
        }
        tag_list = render_to_string('ajax/office/tag_list.html', context2)
        context={
            'tag':tag
        }
        t = render_to_string('ajax/office/generate_tag.html', context)
    return JsonResponse({'t': t,'tag_list':tag_list})


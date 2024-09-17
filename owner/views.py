from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import *
# Create your views here.
def office_home(request):
    if request.session.has_key('office_mobile'):
        return render(request, 'owner/office/office_home.html')
    else:
        return redirect('login')

def add_employee(request):
    if request.session.has_key('office_mobile'):
        if 'Add_Employee'in request.POST:
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            print(mobile)
            if mobile:
                if Office_employee.objects.filter(mobile=mobile).exists():
                    pass
                else:
                    Office_employee(
                        name = name,
                        mobile = mobile,
                        pin = pin
                    ).save()
                    return redirect('add_employee')
        context={
            'employee':Office_employee.objects.all()
        }
        return render(request, 'owner/office/add_employee.html', context)
    else:
        return redirect('login')

def generate_qr_code(request):
    if request.session.has_key('office_mobile'):
        office_mobile = request.session['office_mobile']
        e = Office_employee.objects.filter(mobile=office_mobile).first()
        if e:
            tag_list = Qr_code.objects.filter().order_by('-id')
            paginator = Paginator(tag_list,1000) 
            page_number = request.GET.get('page')
            tag_list = paginator.get_page(page_number)
            total_pages = tag_list.paginator.num_pages
        context={
            'e':e,
            'tag_list':tag_list,
            'last_page':total_pages,
            'total_page_list':[n+1 for n in range(total_pages)][0:3]
        }
        return render(request, 'owner/office/generate_qr_code.html', context)
    else:
        return redirect('login')

def profile(request):
    if request.session.has_key('office_mobile'):
        office_mobile = request.session['office_mobile']
        e = Office_employee.objects.filter(mobile=office_mobile).first()
        s = ''
        if e:
            if 'edit_profile'in request.POST:
                id = request.POST.get('id')
                shop_name = request.POST.get('shop_name')
                shop_address = request.POST.get('shop_address')
                owner_name = request.POST.get('owner_name')
                mobile = request.POST.get('mobile')
                if id:
                    Shop(
                        id=id,
                       shop_name=shop_name, 
                       shop_address=shop_address, 
                       owner_name=owner_name, 
                       mobile=mobile, 
                    ).save()
                else:
                    Shop(
                       shop_name=shop_name, 
                       shop_address=shop_address, 
                       owner_name=owner_name, 
                       mobile=mobile, 
                    ).save()
                return redirect('profile')
            s = Shop.objects.get(status=1)
        context={
            'e':e,
            's':s
        }
        return render(request, 'owner/office/profile.html', context)
    else:
        return redirect('login')

def valid_to_date(request):
    if request.session.has_key('office_mobile'):
        validity_date = ''
        if 'validity_date'in request.POST:
            id = request.POST.get('id')
            date = request.POST.get('date')
            if id:
                Validity_date(
                    id=id,
                    date=date
                ).save()
                return redirect('valid_to_date')
            else:
                Validity_date(
                    date=date
                ).save()
                return redirect('valid_to_date')
        v = Validity_date.objects.all()
        if v:
            validity_date = Validity_date.objects.get(status=1)
        context={
            'validity_date':validity_date
        }
        return render(request, 'owner/office/valid_to_date.html', context)
    else:
        return redirect('login')




















































































































































































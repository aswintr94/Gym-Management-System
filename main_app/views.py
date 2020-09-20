from django.shortcuts import render,redirect
from main_app.models import Enquiry,Plans,Equipments,Members
from django.http import JsonResponse,HttpResponse
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request,'login_page.html')

def login_success(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'admin' and password == 'admin':
        request.session['username'] = 'admin'
        request.session['password'] = 'admin'
        return redirect(dashboard)
    else:
        messages.error(request,"Check the username and password!")
        return redirect(login)

def about_us(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def dashboard(request):
    if 'username' in request.session:
        enq = Enquiry.objects.all()
        plan = Plans.objects.all()
        equip = Equipments.objects.all()
        members = Members.objects.all()
        len_enq = len(enq)
        len_plan = len(plan)
        len_equip = len(equip)
        len_members = len(members)
        return render(request,'dashboard.html',{'len_enq':len_enq, 'len_plan':len_plan,'len_equip':len_equip,'len_members':len_members})
    else:
        messages.error(request,"Login first")
        return redirect(login)

def add_enquiry(request):
    if 'username' in request.session:
        return render(request,'add_enquiry.html')
    else:
        messages.error(request,"Login first")
        return redirect(login)
    

def view_enquiry(request):
    if 'username' in request.session:
        enq = Enquiry.objects.all()
        return render(request,'view_enquiry.html',{'enq': enq})
    else:
        messages.error(request,"Login first")
        return redirect(login)

def enquiry_submit(request):
    name = request.POST.get('name')
    mobile = request.POST.get('mobile')
    email = request.POST.get('email')
    age = request.POST.get('age')
    gender = request.POST.get('gender')

    new = Enquiry(name=name,mobile=mobile,email=email,age=age,gender=gender)
    new.save()
    return redirect(add_enquiry)
    
def remove_enquiry(request,e_id):
    Enquiry.objects.get(id=e_id).delete()
    return redirect(view_enquiry)

def add_plan(request):
    if 'username' in request.session:
        return render(request,'add_plan.html')
    else:
        messages.error(request,"Login first")
        return redirect(login)

def plan_submit(request):
    plan_name = request.POST.get('plan_name')
    plan_amount = request.POST.get('plan_amount')
    plan_duration = request.POST.get('plan_duration')
    new_plan = Plans(plan_name=plan_name,plan_amount=plan_amount,plan_duration=plan_duration)
    new_plan.save()
    return render(request,'add_plan.html')

def view_plan(request):
    if 'username' in request.session:
        plan = Plans.objects.all()
        return render(request,'view_plan.html',{'plan': plan})
    else:
        messages.error(request,"Login first")
        return redirect(login)

def remove_plan(request,plan_id):
    Plans.objects.filter(id=plan_id).delete()
    return redirect(view_plan)

def add_equipment(request):
    if 'username' in request.session:
        return render(request,'add_equipment.html')
    else:
        messages.error(request,"Login first")
        return redirect(login)

def equipment_submit(request):
    eq_name = request.POST.get('equipment_name')
    eq_price = request.POST.get('equipment_price')
    units = request.POST.get('units')
    purchased_date = request.POST.get('purchased_date')
    description = request.POST.get('description')

    new_equipment = Equipments(equipment_name=eq_name,equipment_price=eq_price,unit=units,purchased_date=purchased_date,description=description)
    new_equipment.save()
    return redirect(add_equipment)

def view_equipment(request):
    if 'username' in request.session:
        equipment = Equipments.objects.all()
        return render(request,'view_equipment.html',{'equipment':equipment})
    else:
        messages.error(request,"Login first")
        return redirect(login)

def delete_equipment(request,e_id):
    Equipments.objects.filter(id=e_id).delete()
    return redirect(view_equipment)

def add_member(request):
    if 'username' in request.session:
        plan = Plans.objects.all()
        return render(request,'add_member.html',{'plan':plan})
    else:
        messages.error(request,"Login first")
        return redirect(login)

def submit_member(request):
    name = request.POST.get('name')
    mobile = request.POST.get('mobile')
    email = request.POST.get('email')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    plan = request.POST.get('plan')
    joining_date = request.POST.get('joining_date')
    joining_date_obj = datetime.strptime(joining_date,"%Y-%m-%d")
    plan_check = Plans.objects.get(plan_name=plan)
    period_of_plan = plan_check.plan_duration
    expiry_date = joining_date_obj + relativedelta(months=+period_of_plan)
    initial_amount = request.POST.get('initial_amount')
    new_member = Members(member_name=name,mobile=mobile,email=email,age=age,gender=gender,plan=plan,joining_date=joining_date_obj,plan_expiry_date=expiry_date,initial_amount=initial_amount)
    new_member.save()
    return redirect(add_member)

def view_member(request):
    if 'username' in request.session:
        member = Members.objects.all()
        return render(request,'view_member.html',{'members':member})
    else:
        messages.error(request,"Login first")
        return redirect(login)

def remove_member(request,m_id):
    Members.objects.filter(id=m_id).delete()
    return redirect(view_member)

def log_out(request):
    del request.session['username']
    del request.session['password']
    return redirect(login)

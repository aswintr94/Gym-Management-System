from django.shortcuts import render,redirect
from main_app.models import Enquiry,Plans
from django.http import JsonResponse,HttpResponse

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

def about_us(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def dashboard(request):
    if 'username' in request.session:
        enq = Enquiry.objects.all()
        plan = Plans.objects.all()
        len_enq = len(enq)
        len_plan = len(plan)
        return render(request,'dashboard.html',{'len_enq':len_enq, 'len_plan':len_plan})
    else:
        return redirect(login)

def add_enquiry(request):
    return render(request,'add_enquiry.html')

def view_enquiry(request):
    enq = Enquiry.objects.all()
    return render(request,'view_enquiry.html',{'enq': enq})

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
    return render(request,'add_plan.html')

def plan_submit(request):
    plan_name = request.POST.get('plan_name')
    plan_amount = request.POST.get('plan_amount')
    plan_duration = request.POST.get('plan_duration')
    new_plan = Plans(plan_name=plan_name,plan_amount=plan_amount,plan_duration=plan_duration)
    new_plan.save()
    return render(request,'add_plan.html')

def view_plan(request):
    plan = Plans.objects.all()
    return render(request,'view_plan.html',{'plan': plan})

def remove_plan(request,plan_id):
    Plans.objects.filter(id=plan_id).delete()
    return redirect(view_plan)
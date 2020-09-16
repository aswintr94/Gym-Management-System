from django.shortcuts import render,redirect
from main_app.models import Enquiry
from django.http import JsonResponse,HttpResponse

# Create your views here.
def login(request):
    return render(request,'login_page.html')

def login_success(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'admin' and password == 'admin':
        return render(request,'dashboard.html')

def about_us(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def dashboard(request):
    enq = Enquiry.objects.all()
    len_enq = len(enq)
    return render(request,'dashboard.html',{'len_enq':len_enq})

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

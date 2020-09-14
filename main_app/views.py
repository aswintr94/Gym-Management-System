from django.shortcuts import render,redirect

# Create your views here.
def login(request):
    return render(request,'login_page.html')

def login_success(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'admin' and password == 'admin':
        return redirect(dashboard)

def about_us(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def dashboard(request):
    return render(request,'dashboard.html')

def add_enquiry(request):
    return render(request,'add_enquiry.html')

def view_enquiry(request):
    return render(request,'view_enquiry.html')

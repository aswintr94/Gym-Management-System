from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login_page.html')

def about_us(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def dashboard(request):
    return render(request,'dashboard.html')
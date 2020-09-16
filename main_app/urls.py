from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('login_success/',views.login_success,name='login_success'),
    path('about_us/',views.about_us,name='about_us'),
    path('contact/',views.contact,name='contact'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('add_enquiry/',views.add_enquiry,name='add_enquiry'),
    path('view_enquiry/',views.view_enquiry,name='view_enquiry'),
    path('enquiry_submit/',views.enquiry_submit,name='enquiry_submit'),
    path('remove_enquiry/<int:e_id>',views.remove_enquiry,name='remove_enquiry'),
]
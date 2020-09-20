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
    path('add_plan/',views.add_plan,name='add_plan'),
    path('plan_submit/',views.plan_submit,name='plan_submit'),
    path('view_plan/',views.view_plan,name='view_plan'),
    path('remove_plan/<int:plan_id>',views.remove_plan,name='remove_plan'),
    path('add_equipment/',views.add_equipment,name='add_equipment'),
    path('equipment_submit/',views.equipment_submit,name='equipment_submit'),
    path('view_equipment/',views.view_equipment,name='view_equipment'),
    path('delete_equipment/<int:e_id>',views.delete_equipment,name='delete_equipment'),
    path('add_member/',views.add_member,name='add_member'),
    path('submit_member/',views.submit_member,name='submit_member'),
    path('view_member/',views.view_member,name='view_member'),
    path('remove_member/<int:m_id>',views.remove_member,name='remove_member'),
    path('log_out/',views.log_out,name='log_out'),
]
from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('employees', views.employees, name='employees'),
    path('employees/<int:employee_id>/edit/', views.get_employee_data, name='get_employee_data'),
    path('employees/<int:employee_id>/update/', views.update_employee, name='update_employee'),
    path('employees/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),
    path('generate_employee_list', views.generate_employee_list,name='generate_employee_list'),
    path('advance', views.advance, name='advance'),
    path('advance/<int:advance_id>/edit/', views.get_advance_data, name='get_advance_data'),
    path('advance/<int:advance_id>/update/', views.update_advance, name='update_advance'),
    path('advance/<int:advance_id>/delete/', views.delete_advance ,name='delete_advance'),
    path('deductions', views.deductions, name='deductions'),
    path('deductions/<int:deduction_id>/edit/', views.get_deduction_data, name='get_deduction_data'),
    path('deductions/<int:deduction_id>/update/', views.update_deduction, name='update_deduction'),
    path('deductions/<int:deduction_id>/delete/', views.delete_deductions, name='delete_deductions'),
    path('arrears', views.arrears, name='arrears'),
    path('arrears/<int:arrears_id>/edit/', views.get_arrears_data, name='get_arrears_data'),
    path('arrears/<int:arrears_id>/update/', views.update_arrears, name='update_arrears'),
    path('arrears/<int:arrears_id>/delete', views.delete_arrears, name='delete_arrears'),
    path('generate_payslip/<int:employee_id>', views.generate_payslip, name='generate_payslip'),
    path('payroll_report' ,views.payroll_report, name='payroll_report'),
    path('excel_report', views.excel_report, name='excel_report'),
    path('logout', views.log_out, name='log_out'),
]

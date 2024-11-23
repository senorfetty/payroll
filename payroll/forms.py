from django import forms
from .models import Employee, Advance,Deduction,Arrears

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ['first_name','last_name','phone_number','gender','area_of_work','id_number','days_worked','salary']
        widgets= {
            'gender': forms.Select(choices=[('male','Male'), ('female','Female')]),
            'id_number': forms.NumberInput(attrs={'min':0,'step': '1'}),
            'days_worked': forms.Select(choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21','21'),('22','22'),('23','23'),('24','24'),('25','25'),('26','26'),('27','27'),('28','28'),('29','29'),('30','30')]),
            'salary': forms.NumberInput(attrs={'min':0,'step': '1'})
        }
        
class AdvanceForm(forms.ModelForm):
    class Meta:
        model= Advance
        fields = ['employee', 'amount', 'date']
        widgets = {
            'employee' : forms.Select(),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'amount' : forms.NumberInput(attrs={'min': 0,'step': '1'})
        }
        
class DeductionForm(forms.ModelForm):
    class Meta:
        model = Deduction
        fields = ['employee','nhif','nssf','uniform','fuel']
        widgets = {
            'employee': forms.Select(),
            'nhif' : forms.NumberInput(attrs={'min': 0,'step': '1'}),
            'nssf' : forms.NumberInput(attrs={'min': 0,'step': '1'}),
            'uniform' : forms.NumberInput(attrs={'min': 0,'step': '1'}),
            'fuel' : forms.NumberInput(attrs={'min': 0,'step': '1'})
        }
        
class ArrearsForm(forms.ModelForm):
    class Meta:
        model= Arrears
        fields = ['employee','amount','month']
        widgets = {
            'employee': forms.Select(),
            'amount' : forms.NumberInput(attrs={'min':0,'step': '1'}),
            'month' : forms.Select(choices=[('January','January'),('February','February'),('March', 'March'),('April','April'),('May', 'May'),('June', 'June'),('July', 'July'),('August', 'August'),('September', 'September'),('October', 'October'),('November', 'November'),('December', 'December')])
        }                                                                                  
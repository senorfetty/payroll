from django.db import models
from django.utils import timezone
from django.db.models import Sum

# Create your models here.


class Employee(models.Model):
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    DAYS_WORKED = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
        ('13','13'),
        ('14','14'),
        ('15','15'),
        ('16','16'),
        ('17','17'),
        ('18','18'),
        ('19','19'),
        ('20','20'),
        ('21','21'),
        ('22','22'),
        ('23','23'),
        ('24','24'),
        ('25','25'),
        ('26','26'),
        ('27','27'),
        ('28','28'),
        ('29','29'),
        ('30','30')
    ]
    employee_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name= models.CharField(max_length=40)
    phone_number= models.CharField(max_length=20)
    gender= models.CharField(choices=GENDER, max_length=10)
    area_of_work = models.CharField(max_length=100)
    id_number = models.CharField(max_length=50)
    days_worked = models.CharField(choices=DAYS_WORKED,max_length=10)   
    salary= models.DecimalField(max_digits=100, decimal_places=2)    
    
    
    @property
    def net_pay(self):
        advances_total= Advance.objects.filter(employee=self).aggregate(Sum('amount'))['amount__sum'] or 0
        arreas_total= Arrears.objects.filter(employee=self).aggregate(Sum('amount'))['amount__sum'] or 0
        deductions_total = Deduction.objects.filter(employee=self).aggregate(
            nhif=Sum('nhif') or 0,
            nssf=Sum('nssf') or 0,
            uniform=Sum('uniform') or 0,
            fuel=Sum('fuel') or 0
        )
        
        deductions_sum = sum(value or 0 for value in deductions_total.values())

        
        return self.salary - advances_total - deductions_sum + arreas_total
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Advance(models.Model):
    employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount= models.DecimalField(max_digits=100, decimal_places=2)
    date = models.DateField()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} = {self.amount}'
    
class Deduction(models.Model):
    employee= models.ForeignKey(Employee, on_delete= models.CASCADE)
    nhif= models.CharField(max_length=50)
    nssf= models.CharField(max_length=50)
    uniform= models.CharField(max_length=50)
    fuel= models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Arrears(models.Model):
    month = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]
    employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2,max_digits=100)
    month = models.CharField(choices=month, max_length=20)
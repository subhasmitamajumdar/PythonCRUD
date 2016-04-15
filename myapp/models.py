from django.db import models

# Create your models here.
from django.core.validators import RegexValidator


class Employee(models.Model):
    number_regex=RegexValidator(regex=r'[0-9]*',message="only numeric values allowed")
    name_regex=RegexValidator(regex=r'^[A-Za-z][^A-Z]*$', message="name should contain only characters")
    emp_id=models.CharField(max_length=3,validators=[number_regex],primary_key=True)
    emp_name=models.CharField(max_length=30,validators=[name_regex])
    emp_age=models.CharField(max_length=2,validators=[number_regex])
    dept_id=models.CharField(max_length=3,validators=[number_regex])

    def __unicode__(self):
        return str(self.user.username)

class Department(models.Model):
    name_regex=RegexValidator(regex=r'^[A-Za-z][^A-Z]*$', message="name should contain only characters")
    number_regex=RegexValidator(regex=r'[0-9]*',message="only numeric values allowed")
    dept_id=models.CharField(max_length=3,validators=[number_regex],primary_key=True)
    dept_name=models.CharField(max_length=30,validators=[name_regex], unique=True)
    emp_id=models.CharField(max_length=3,validators=[number_regex],unique=False,null=False,blank=True)

    #foreign key relation not working!
    #emp_id=models.ForeignKey(Employee,on_delete=models.CASCADE)

    def __unicode__(self):
        return str(self.dept_name)
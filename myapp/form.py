from django import forms
from .models import Employee,Department

class EmployeeRegisterForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['emp_id','emp_name','emp_age','dept_id']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields=['dept_id','dept_name','emp_id']

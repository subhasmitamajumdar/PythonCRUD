from django.shortcuts import render, redirect, get_object_or_404
from .form import EmployeeRegisterForm,DepartmentForm
from .models import Employee,Department

def emp_list(request, template_name='emp_list.html'):
    employee = Employee.objects.all()
    data = {}
    data['eobject_list'] = employee
    return render(request, template_name, data)

def dept_list(request, template_name='dept_list.html'):
    department = Department.objects.all()
    data = {}
    data['dobject_list'] = department
    return render(request, template_name, data)

def emp_create(request, template_name='emp_form.html'):
        eform=EmployeeRegisterForm(request.POST or None)
        if eform.is_valid():
            eform.save()
            return redirect('emp_list')
        return render(request, template_name,{'eform':eform})

def dept_create(request, template_name='dept_form.html'):
        dform=DepartmentForm(request.POST or None)
        if dform.is_valid():
            dform.save()
            return redirect('dept_list')
        return render(request, template_name,{'dform':dform})


def emp_update(request, pk, template_name='emp_form.html'):
    emp_update = get_object_or_404(Employee, pk=pk)
    eform = EmployeeRegisterForm(request.POST or None, instance=emp_update)
    if eform.is_valid():
        eform.save()
        return redirect('emp_list')
    return render(request, template_name, {'eform':eform})

def dept_update(request, pk, template_name='dept_form.html'):
    dept_update = get_object_or_404(Department, pk=pk)
    dform = DepartmentForm(request.POST or None, instance=dept_update)
    if dform.is_valid():
        dform.save()
        return redirect('dept_list')
    return render(request, template_name, {'dform':dform})

def emp_delete(request, pk, template_name='emp_confirm_delete.html'):
    emp_delete = get_object_or_404(Employee, pk=pk)
    if request.method=='POST':
        emp_delete.delete()
        return redirect('emp_list')
    return render(request, template_name, {'object':emp_delete})

def dept_delete(request, pk, template_name='dept_confirm_delete.html'):
    dept_delete = get_object_or_404(Department, pk=pk)
    if request.method=='POST':
        dept_delete.delete()
        return redirect('dept_list')
    return render(request, template_name, {'object':dept_delete})
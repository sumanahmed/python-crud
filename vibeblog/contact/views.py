from django.shortcuts import render, redirect
from contact.models import Employee
from . forms import EmployeeForm

# Create your views here.
def contact(request):
    return render(request, 'pages/contact.html')

def list(request):
    employees = Employee.objects.all()
    return render(request, 'pages/crud/list.html', {'data': employees})

def create(request):
    formData = EmployeeForm()
    return render(request, 'pages/crud/create.html', { 'form': formData })

def store(request):
    if request.method == "POST": 
        form = EmployeeForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/contact/crud-list')
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'pages/crud/create.html',{'form':form})

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'pages/crud/edit.html', {'item':employee})

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect('/contact/crud-list')
    return render(request, 'pages/crud/edit.html', {'employee': employee})  

def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect('/contact/crud-list')
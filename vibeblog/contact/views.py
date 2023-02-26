from django.shortcuts import render, redirect
from contact.models import Employee
from . forms import EmployeeForm
import cx_Oracle

# Create your views here.
def connection():
    h = 'localhost' #Your host name/ip
    p = '1521' #Your port number
    sid = 'ORCL' #Your sid
    u = 'python_db' #Your login user name
    pw = '123456' #Your login password
    d = cx_Oracle.makedsn(h, p, sid=sid)
    conn = cx_Oracle.connect(user=u, password=pw, dsn=d)
    return conn

def contact(request):
    return render(request, 'pages/contact.html')

def list(request):
    employees = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    for row in cursor.fetchall():
        employees.append({"id": row[0], "ename": row[1], "econtact": row[2], "eemail": row[3]})
    conn.close()
    return render(request, 'pages/crud/list.html', {'data': employees})

def create(request):
    formData = EmployeeForm()
    return render(request, 'pages/crud/create.html', { 'form': formData })

def store(request):
    if request.method == "POST": 
        form = EmployeeForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get("id")
            ename = form.cleaned_data.get("ename")
            econtact = form.cleaned_data.get("econtact")
            eemail = form.cleaned_data.get("eemail")
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO employees VALUES (:id, :ename, :econtact, :eemail)", [id, ename, econtact, eemail])
            conn.commit()
            conn.close()
        return redirect('/contact/crud-list')
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
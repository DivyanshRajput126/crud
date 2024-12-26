from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def InsertPageView(request):
    return render(request,"app/insert.html")

def InsertDataView(request):
    # Data came from html form
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    phone = request.POST['phone']
    
    # Creating object of model class
    # Inserting data into table
    newUser = Student.objects.create(FirstName = fname, LastName = lname, Email = email, Contact = phone)
    # After Insert on show.html
    return redirect("showpage")

def ShowPage(request):
    # select * from table name
    # For fetching all data from database we will fire all method of student.object
    all_data = Student.objects.all()
    return render(request,"app/show.html",{'key1':all_data})

def EditPage(request,pk):
    #Fetching data of perticular id
    get_data = Student.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':get_data})

#Update Data View
def UpdateData(request,pk):
    udata = Student.objects.get(id=pk)
    udata.FirstName = request.POST['fname']
    udata.LastName = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['phone']
    udata.save()
    return redirect("showpage")

# Deleting User
def DeleteData(request,pk):
    ddata = Student.objects.get(id=pk)
    ddata.delete()
    return redirect("showpage")
from django.shortcuts import render,HttpResponseRedirect
from .forms import studentregistration

# Create your views here.
from .models import  user

# this function add new and show all item
def addshow(request):
    if request.method=='POST':
        f=studentregistration(request.POST)
        if  f.is_valid():
            nm=f.cleaned_data['name']
            em=f.cleaned_data['email']
            pw=f.cleaned_data['password']
            gen=f.cleaned_data['gender']
            bd=f.cleaned_data['birth_date']
            # creating a object of user table
            reg=user(name=nm,email=em,password=pw,gender=gen,birth_date=bd)
            reg.save()
            f=studentregistration()                 # blank form
            # f.save()
    else:
            f=studentregistration()

    stud=user.objects.all()                                 #showing data in home page of database
    return render(request,'student/show.html',{'form':f,'stu':stud})

# function  will  delete data
def delete_data(request,id):
    if request.method=='POST':
        pi=user.objects.get(pk=id)
        pi.delete()
        return  HttpResponseRedirect('/')

# update  fuction will update  data  specifiec id
def update_data(request,id):
    # return render(request, 'student/update.html', {'id': id})         # it return specific id
    if request.method=="POST":
        pi=user.objects.get(pk=id)
        fm=studentregistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()

    # jab update pr  click na ho  to get method
    # Get ------>
    else:
        pi=user.objects.get(pk=id)
        fm=studentregistration(instance=pi)
    return render(request,'student/update.html',{'form':fm})
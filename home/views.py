from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import addImg
# Create your views here.
def home(request):
    data=addImg.objects.all()
    context={'data':data}
    # if request.method=='POST':
    #     form=ImageForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    # form=ImageForm()
    if request.method=='POST':
        name=request.POST['app']
        points=request.POST['points']
        photo=request.FILES['text_1']
        addImg(photo=photo, name=name, points=points).save()
    return render(request,'home.html', context)

def userPage(request):
    data=addImg.objects.all()
    context={"data":data}
    return render(request,'user.html', context)

# def addItem(request):
#     if request.method=='POST':
#         img=request.FILES['image']
#         addImage(img=img).save()
#     return render(request,'add.html')
def appData(request, app_Id):
    data=addImg.objects.get(id=app_Id)
    context={'data':data}
    return render(request,'appData.html',context)

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        Password=request.POST['password']
        myuser=User.objects.create_user(username,email,Password)
        myuser.save()
        messages.success(request,'Registered successfully...')
        return redirect('login')

    return render(request,'signup.html')

def log(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('home')
            else:
                return redirect('user')
            # return redirect('home')
        else:
            messages.warning(request,'Invalid Username or Password')
    return render(request,'login.html')

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')
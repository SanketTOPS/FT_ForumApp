import re
from django.shortcuts import redirect, render
from .forms import signupForm, notesForm,contactForm
from .models import signup_master
from django.contrib.auth import logout
from django.core.mail import send_mail
from BatchProject import settings
import requests
import json
import random

# Create your views here.
"""
def userSignup(request):
    newuser=signupForm(request.POST)
    if newuser.is_valid():
        newuser.save()
        print("User created successfully!")
    else:
        print(newuser.errors)"""
        
"""def userSignin(request):
    unm=request.POST["username"]
    pas=request.POST["password"]

    user=signup_master.objects.filter(username=unm,password=pas)
    if user: #true
        print("Login successfully!")
    else:
        print("Error....Login fail, Try again.")"""


def index(request):
    if request.method=="POST":
        if request.POST.get("login")=="login":
            unm=request.POST["username"]
            pas=request.POST["password"]
            user=signup_master.objects.filter(username=unm,password=pas)

            userid=signup_master.objects.get(username=unm)
            print("UserID:",userid.id)

            
            if user:
                print("Login Successfull!")
                request.session["user"]=unm
                request.session["userid"]=userid.id

                # Send SMS Code
                otp=random.randint(1111,9999)
                url = "https://www.fast2sms.com/dev/bulkV2"
                querystring = {"authorization":"PSqGhvu5BkQv1WEvvWH6PIgV0vr1IcOIEzgsN1fZMHFG0WJapJ1hGGIwYfq8","message":f"Hello User, Your account has been login!\n Your OTP is {otp}","language":"english","route":"q","numbers": "7990341676,9426913979,9316312117"}

                headers = {
                    'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)
                return redirect("notes")
            else:
                print("Error...Login fail! Try again.")
        elif request.POST.get("signup")=="signup":
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("User created successfully!")

                # Send EMAIL
                sub="Welcome!"
                msg=f"Dear User!\nYour account has been created with us.\nEnjoy our services with your requirements.\nFor any query, Call us,\n+91 9724799469 | sanket@gmail.com"
                #from_id="sanket.tops@gmail.com"
                from_id=settings.EMAIL_HOST_USER
                #to_id=["viralranipa11@gmail.com"]
                to_id=[request.POST["username"]]
                send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)

                return redirect("notes")
            else:
                print(newuser.errors)
    return render(request,'index.html')


def notes(request):
    user=request.session.get("user")
    if request.method=="POST":
        mynote=notesForm(request.POST, request.FILES)
        if mynote.is_valid():
            mynote.save()
            print("Your post has been uploaded!")
        else:
            print(mynote.errors)
    return render(request,'notes.html',{'user':user})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        cont=contactForm(request.POST)
        if cont.is_valid():
            cont.save()
            print("Your msg has been sent successfully!")
        else:
            print(cont.errors)  
    return render(request,'contact.html')

def userlogout(request):
    logout(request)
    return redirect("/")

def updateprofile(request):
    user=request.session.get("user")
    userid=request.session.get("userid")
    uid=signup_master.objects.get(id=userid)
    if request.method=="POST":
        updateuser=signupForm(request.POST)
        if updateuser.is_valid():
            updateuser=signupForm(request.POST,instance=uid)
            updateuser.save()
            print("Your profile has been updated!")
            return redirect("notes")
        else:
            print(updateuser.errors)
    return render(request,'updateprofile.html',{'user':user,"cuser":signup_master.objects.get(id=userid)})
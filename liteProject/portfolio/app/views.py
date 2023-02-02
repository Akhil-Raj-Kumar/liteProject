from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.contrib import messages

#Registration
def registration_page(req):
    return render(req,"register.html")

def register(req):
    if req.method == 'POST':
        if 'n4' in req.POST:
            print("Key is there")
        d=req.POST['n1']
        e=User.objects.filter(name=d)
        if e.exists() == False:
            a=req.POST['n1']
            b=req.POST['n2']
            c=req.POST['n3']
            d=req.FILES['n4']
            data=User(name=a,email=b,password=c,profile_pic=d)
            data.save()
            return redirect('/login_page/')
        else:
            print("This is else part")
            return render(req, "register.html",{"error_msg": "Username already exists!"})
            #return messages.info(req, "Username already exists!")
    else:
        return HttpResponse("Start from Registration Page")


#Login
def loginPage(req):
    return render(req,"login.html")

def login(req):
    if req.method == 'POST':
        User_logged.objects.all().delete()
        a=req.POST['n1']
        b=req.POST['n2']
        c = User.objects.get(name=a)
        if c.password == b:
            data=User_logged(pswd=b)
            data.save()
            return redirect('/home_page/')
        else:
            return render(req, "login.html",{"error_msg":"Incorrect username or password"})

#Home
def home(req):
    pData=Products.objects.all()
    return render(req,"home.html", {'products':pData})

#User
def user_delete(req,a):
    u=User.objects.filter(name=a)
    u.delete()
    return redirect('/home_page/')

def product_del(req,a):
    p=Products.objects.filter(p_name=a)
    p.delete()
    return redirect('/home_page/')

def userPage(req):
    uData=User.objects.all()
    uLog=User_logged.objects.all()
    return render(req,'userProfiles.html',{'userDetails':uData,'userLogged':uLog})

#Profile_Picture
# def updateProfilePic(req):
#     if req.method == 'POST':
#         a=req.FILES.get('pro_pic')
#         data=User(profile_pic=a)
#         data.save()
#         return redirect(userPage)


#Products
def productPage(req):
    return render(req,'products.html')

def addProduct(req):
    if req.method == 'POST':
        pName=req.POST['pName']
        pID=int(req.POST['pID'])
        pImg=req.FILES['pImage']
        price=int(req.POST['price'])
        data=Products(img=pImg,p_name=pName,p_id=pID,p_price=price)
        data.save()
        return redirect(home)









import os

from django.shortcuts import render, redirect

import smtplib
from urllib import request
from organization.settings import BASE_DIR
from django.shortcuts import render
from django.urls import reverse


from user.models import userlogin



# Create your views here.
def login(request):
    if request.method == 'POST':
        print("Login function called")  # DEBUG

        username = request.POST.get('t1', '').strip().lower()
        password = request.POST.get('t2', '').strip()

        try:
            user = userlogin.objects.get(username=username)

            if user.password == password:
                request.session['username'] = username

                if user.utype == 'admin':
                    return render(request, 'organization_home.html')

                elif user.utype == 'customer':
                    return render(request, 'user_home.html')

            else:
                return render(request, 'login.html', {'msg1': 'Incorrect password'})

        except userlogin.DoesNotExist:
            return render(request, 'login.html', {'msg2': 'Incorrect email'})

    return render(request, 'login.html')

from django.shortcuts import render
from .models import newuser, userlogin, match_details, PlayerDetails, awards, user_details, player_statics, \
    match_statics, organizer
import smtplib

from django.shortcuts import render
from .models import newuser, userlogin
import smtplib

def insertnewuser(request):
    if request.method == "POST":
        s1 = request.POST.get("t1", '').strip()
        mailid = request.POST.get("t2", '').strip().lower()
        mobileno = request.POST.get("t3", '').strip()
        city = request.POST.get("t5", '').strip()
        password = request.POST.get("t4", '').strip()

        # ✅ Empty validation
        if not (s1 and mailid and mobileno and city and password):
            return render(request, "reg.html", {"msg": "All fields are required!"})

        # ✅ Duplicate check
        if newuser.objects.filter(emailid=mailid).exists() or \
           userlogin.objects.filter(username=mailid).exists():
            return render(request, "reg.html", {"msg": "Email already registered!"})

        # ✅ Save user
        newuser.objects.create(
            username=s1,
            emailid=mailid,
            mobileno=mobileno,
            city=city
        )

        userlogin.objects.create(
            username=mailid,
            password=password,
            utype='customer'
        )

        # ✅ Send email (safe)
        try:
            msg = f"Hello {s1}, your password is {password}"

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('gv161877@gmail.com', 'vhkr bpsm hlnk klgy')
            server.sendmail('gv161877@gmail.com', mailid, msg)
            server.quit()

        except Exception as e:
            print("Email error:", e)

        return render(request, "login.html", {"msg": "Registered successfully! Please login."})

    return render(request, "reg.html")


def forgotpassword(request):
    if request.method=="POST":
        uname = request.POST.get('t1', '')
        user = userlogin.objects.filter(username=uname).count()
        if user >= 1:
            userlog = userlogin.objects.filter(username=uname).values()
            for u in userlog:
                upass= u['password']
                content = upass
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login('gv161877@gmail.com', 'vhkr bpsm hlnk klgy')
                mail.sendmail('gv161877@gmail.com', uname , content)
                mail.close()
                return render(request,'login.html', {'msg': 'Your password has been sent to your E-mail'})
        else:
            return render(request,'forgot4.html', {'msg': 'Enter a valid username'})
    return render(request,'forgot4.html')

def showuser(request):
    if request.method == 'POST':
        return render(request,'user5.html')
    return render(request,'user5.html')

def showadmin(request):
    if request.method == 'POST':
        return render(request,'admin6.html')
    return render(request,'admin6.html')

def showindex(request):
    if request.method == 'POST':
        return render(request,'home.html')
    return render(request,'home.html')


def sendmail(request):
    if request.method == "POST":
        to = request.POST.get('t1')
        message=request.POST.get('t2')

        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('gv161877@gmail.com', 'xzvv jmol mhuc xezv')
        mail.sendmail('gv161877@gmail.com',to, message)
        mail.close()
        return render(request, 'sendmail.html')
    return render(request, 'sendmail.html')


def changepassword(request):
    uname=request.session.get('username')
    if request.method == 'POST':
        oldpass = request.POST.get('t1','')
        newpass = request.POST.get('t2','')
        confirmpass = request.POST.get('t3','')

        ucheck = userlogin.objects.filter(username=uname).values()
        for a in ucheck:
            u = a['username']
            p = a['password']
            if u == uname and oldpass == p:
                if newpass == confirmpass:
                    userlogin.objects.filter(username=uname).update(password=newpass)
                    base_url=reverse('login')
                    msg1='password has been changed successfully'
                    return redirect(base_url,msg=msg1)
                else:
                    return render(request, 'changepassword.html',{'msg2': 'both the username and password are incorrect'})
            else:
                return render(request, 'changepassword.html')
    return render(request, 'changepassword.html')

# Table 1
def addorganizer(request):
    if request.method=="POST":
        s1=request.POST.get("t1")
        s3=request.POST.get("t3")
        s4=request.POST.get("t4")
        s5=request.POST.get("t5")
        organizer.objects.create(match_details=s1,suspect_details=s3,add_players=s4,team_details=s5)
        return render(request,"organizer.html")
    return render(request,"organizer.html")

def vieworganizer(request):
    userdict=organizer.objects.all()
    return render(request,"vieworganizer.html",{'userdict':userdict})

def delorganizer(request,pk):
    id = organizer.objects.get(id=pk)
    id.delete()
    userdict = organizer.objects.all()
    return render(request, "vieworganizer_1.html", {'userdict': userdict})


#Table 2

def addmatch_details(request):
    if request.method=="POST":
        s1=request.POST.get("t1")
        s2=request.POST.get("t2")
        s3=request.POST.get("t3")
        s4=request.POST.get("t4")
        s5=request.POST.get("t5")
        s6=request.POST.get("t6")
        s7=request.POST.get("t7")
        match_details.objects.create(match_no=s1,ipl_no=s2,date=s3,venue=s4,team1=s5,team2=s6,start_time=s7)
        s1 = match_details.objects.all().order_by('match_no').last()
        s1 = int(s1.match_no) + 1
        return render(request,"match_details.html",{'s1':s1})
    s1 = match_details.objects.all().order_by('match_no').last()
    s1 = int(s1.match_no) + 1
    return render(request,"match_details.html",{'s1':s1})

def viewmatch_details(request):
    userdict=match_details.objects.all()
    return render(request,"viewmatch_details.html",{'userdict':userdict})

def delmatch_details(request,pk):
    id = match_details.objects.get(id=pk)
    id.delete()
    userdict=match_details.objects.all()
    return render(request,"viewmatchdetails_2.html",{'userdict':userdict})

#Table 3
from django.shortcuts import render
from .models import PlayerDetails

def addplayer_details(request):
    if request.method == "POST":
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s8 = request.POST.get("t8")

        # Safe file handling
        photo = request.FILES.get('myfile')

        # Save data
        PlayerDetails.objects.create(
            player_id=s1,
            name=s2,
            address=s3,
            age=s5,
            player_type=s6,
            photo=photo,
            debut=s8
        )

        # Generate next player_id
        last = PlayerDetails.objects.all().order_by('player_id').last()
        next_id = int(last.player_id) + 1 if last else 1

        return render(request, "playerdetails.html", {'s1': next_id})

    # GET request
    last = PlayerDetails.objects.all().order_by('player_id').last()
    next_id = int(last.player_id) + 1 if last else 1

    return render(request, "playerdetails.html", {'s1': next_id})
def viewplayer_details(request):
    userdict=PlayerDetails.objects.all()
    return render(request,"viewplayer_details.html",{'userdict':userdict})

def delplayer_details(request,pk):
    id = PlayerDetails.objects.get(id=pk)
    id.delete()
    userdict = PlayerDetails.objects.all()
    return render(request, "viewplayer_details.html", {'userdict': userdict})

#Table 4

def addawards(request):
    if request.method=="POST":
        s1=request.POST.get("t1")
        s2=request.POST.get("t2")
        s3=request.POST.get("t3")
        awards.objects.create(player_id=s1,award_name=s2,date=s3)
        s1 = awards.objects.all().order_by('player_id').last()
        s1 = int(s1.player_id) + 1
        return render(request,"awards.html",{'s1':s1})
    s1 = awards.objects.all().order_by('player_id').last()
    s1 = int(s1.player_id) + 1
    return render(request,"awards.html",{'s1':s1})


def viewawards(request):
    userdict=awards.objects.all()
    return render(request,"viewawards.html",{'userdict':userdict})

def delawards(request,pk):
    id = awards.objects.get(id=pk)
    id.delete()
    userdict = awards.objects.all()
    return render(request, "viewawards.html", {'userdict': userdict})

#Table 5

def adduser_details(request):
    if request.method=="POST":
        s1=request.POST.get("t1")
        s2=request.POST.get("t2")
        s3=request.POST.get("t3")
        s4=request.POST.get("t4")
        s5=request.POST.get("t5")
        s6=request.POST.get("t6")
        user_details.objects.create(user_id=s1,name=s2,address=s3,email_id=s4,adhaar_no=s5,mobile_no=s6)
        s1 = user_details.objects.all().order_by('user_id').last()
        s1 = int(s1.user_id) + 1
        return render(request,"user_details.html",{'s1':s1})
    s1 = user_details.objects.all().order_by('user_id').last()
    s1 = int(s1.user_id) + 1
    return render(request,"user_details.html",{'s1':s1})

def viewuser_details(request):
    userdict=user_details.objects.all()
    return render(request,"viewuser_details.html",{'userdict':userdict})

def deluser_details(request,pk):
    id = user_details.objects.get(id=pk)
    id.delete()
    userdict=user_details.objects.all()
    return render(request,"viewuser_details.html",{'userdict':userdict})
#Table 6

def addtplayer_statics(request):
    if request.method=="POST":
        s1=request.POST.get("t1")
        s2=request.POST.get("t2")
        s3=request.POST.get("t3")
        s4=request.POST.get("t4")
        s5=request.POST.get("t5")
        s6=request.POST.get("t6")
        player_statics.objects.create(player_id=s1,match_id=s2,total_score=s3,no_of_catches=s4,no_of_wickets=s5,awards=s6)
        s1 = player_statics.objects.all().order_by('player_id').last()
        s1 = int(s1.player_id) + 1
        return render(request,"player_statics.html",{'s1':s1})
    s1 = player_statics.objects.all().order_by('player_id').last()
    s1 = int(s1.player_id) + 1
    return render(request,"player_statics.html",{'s1':s1})

def viewplayer_statics(request):
    userdict=player_statics.objects.all()
    return render(request,"viewplayer_statics.html",{'userdict':userdict})

def delplayer_statics(request,pk):
    id = player_statics.objects.get(id=pk)
    id.delete()
    userdict=player_statics.objects.all()
    return render(request,"viewplayer_statics.html",{'userdict':userdict})


#Table 7

def addmatch_statics(request):
    if request.method=="POST":
        s1=request.POST.get("t1")
        s2=request.POST.get("t2")
        s3=request.POST.get("t3")
        s4=request.POST.get("t4")
        s5=request.POST.get("t5")
        s6=request.POST.get("t6")
        s7=request.POST.get("t7")
        s8=request.POST.get("t8")
        s9=request.POST.get("t9")
        s10=request.POST.get("t10")
        match_statics.objects.create(match_id=s1,team1=s2,team2=s3,team1_score=s4,team2_score=s5,captain_team1=s6,captain_team2=s7,result=s8,match_type=s9,no_of_overs=s10)
        s1 = match_statics.objects.all().order_by('match_id').last()
        s1 = int(s1.match_id) + 1
        return render(request,"match_statics.html",{'s1':s1})
    s1 = match_statics.objects.all().order_by('match_id').last()
    s1 = int(s1.match_id) + 1
    return render(request,"match_statics.html",{'s1':s1})

def viewmatch_statics(request):
    userdict=match_statics.objects.all()
    return render(request,"viewmatch_statics.html",{'userdict':userdict})

def delmatch_statics(request,pk):
    id = match_statics.objects.get(id=pk)
    id.delete()
    userdict=match_statics.objects.all()
    return render(request,"viewmatch_statics.html",{'userdict':userdict})

def vieworg(request):
    userdict=organizer.objects.all()
    return render(request,"vieworganizer_1.html",{'userdict':userdict})

def viewmatchdetail(request):
    userdict=match_details.objects.all()
    return render(request,"viewmatchdetails_2.html",{'userdict':userdict})

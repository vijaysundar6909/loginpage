from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import subject, rank


def register(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        uname = request.POST['user_name']
        gmail = request.POST['email']
        password1 = request.POST['password']
        user = User.objects.create_user(first_name =fname, last_name = lname,username = uname,email = gmail,password=password1)
        print("user created")
        user.save()
    return render(request,"reg.html")

def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password1 = request.POST['password']
        user = auth.authenticate(username = uname,password = password1)
        auth.login(request,user)
        print("user login")
        return redirect("/user")
    else:
        return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
#
# def userlogin(request):
#     return render(request,"userlogin.html")

def mark(request):
    if request.method == 'POST':
        mail = request.POST['gmail']
        marks1 = request.POST['english']
        marks2 = request.POST['tamil']
        marks3 = request.POST['maths']
        marks4 = request.POST['science']
        marks5 = request.POST['social']
        tot_mark = subject.objects.create(gmail=mail, english=marks1, tamil=marks2, maths=marks3, science=marks4, social=marks5)
        print("created tot_mark")
        tot_mark.save()
        result1 = int(tot_mark.english) + int(tot_mark.tamil) + int(tot_mark.maths) + int(tot_mark.science) + int(tot_mark.social)
        print(result1)
        total_rank = rank(gmail=tot_mark,total=result1,rank=0)
        print("total_rank")
        total_rank.save()
        return HttpResponse(result1)
    else:
        return render(request,"userlogin.html")

def cal_rank(request):
    z = []
    for i in rank.objects.all().values():
        u = i['id']
        r = i['total']
        z.append(i)
        z = sorted(z, key=lambda k: k["total"], reverse=True)
    print(z)
    to_mar = z
    current_rank = 0
    global_rank = 0
    current_mark = 0
    for ma in to_mar:
        global_rank += 1
        if mark != current_mark:
            current_mark = mark
            current_rank = global_rank
        return current_mark, current_rank
    return HttpResponse(mark)









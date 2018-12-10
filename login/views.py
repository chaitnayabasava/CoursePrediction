# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import authenticate
from .forms import UserForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import Student, FacultyAdvisor
from django.contrib.auth.models import User
import MySQLdb

db = MySQLdb.connect("localhost","root","manasa@6","ase")
# Create your views here.
@csrf_exempt
def login_user(request):
    flag = 0
    if request.method == "POST":
        rollno = request.POST['username']
        password = request.POST['password']
        type_of = request.POST['type']
        #print(rollno, password, type_of)
        cur1 = db.cursor()
        cur1.execute("select * from student where Student_Id='"+rollno+"';")
        a = cur1.fetchall()
        cur2 = db.cursor()
        cur2.execute("select * from employee where Employee_Reg_No='"+rollno+"';")
        b = cur2.fetchall()
        if(type_of == 'Student'):
            if(User.objects.filter(username=rollno).exists()) and a:
            #return render(request,'eclabmanagement/student/index.html')
                user = authenticate(username=rollno, password=password)
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        request.session['type'] = type_of
                        request.session['student'] = rollno
                        print(request.user)
                        return redirect('/student/')
                    else:
                        return render(request, 'login.html', {'status': 'Either your rollno or password are incorrect'})
                else:
                    return render(request, 'login.html', {'status': 'Either your rollno or password are incorrect'})
            elif a:
                student_obj = Student()
                student_obj.roll_no = rollno

                user = User.objects.create_user(username=rollno, password='123456')
                user.save()

                user_id_obj = user
                student_obj.user = user_id_obj
                student_obj.save()
                return render(request, 'login.html', {'status': 'Either your rollno or password are incorrect'})
            else:
                return render(request, 'login.html', {'status': 'The student is not registered.'})

        if(type_of == 'Faculty Advisor'):
            if(User.objects.filter(username=rollno).exists()) and b:
            #return render(request,'eclabmanagement/student/index.html')
                user = authenticate(username=rollno, password=password)
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        request.session['type'] = type_of
                        request.session['employee'] = rollno
                        print(request.user)
                        return redirect('/facultyadv/')
                    else:
                        return render(request, 'login.html', {'status': 'Either your rollno or password are incorrect'})
                else:
                    return render(request, 'login.html', {'status': 'Either your rollno or password are incorrect'})
            elif b:
                student_obj = FacultyAdvisor()
                student_obj.roll_no = rollno

                user = User.objects.create_user(username=rollno, password='123456')
                user.save()

                user_id_obj = user
                student_obj.user = user_id_obj
                student_obj.save()
                return render(request, 'login.html', {'status': 'Either your rollno or password are incorrect'})
            else:
                return render(request, 'login.html', {'status': 'The FA is not registered.'})
        if(type_of == 'Admin'):
            if(User.objects.filter(username=rollno).exists() and rollno == "root" and password == "iamstudent"):
            #return render(request,'eclabmanagement/student/index.html')
                user = authenticate(username=rollno, password=password)
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        request.session['type'] = type_of
                        print(request.user)
                        return redirect('/admin_user/')
                    else:
                        return render(request, 'login.html', {'status': 'Either your rollno or password are incorrect'})
                else:
                    return render(request, 'login.html', {'status': 'Either your UserName or password are incorrect'})
            else:
                return render(request, 'login.html', {'status': 'The Admin is not registered.'})
    return render(request, 'login.html')


"""def signup(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		user  = form.save(commit=False)
        username = form.cleaned_data['username']
        raw_password = form.cleaned_data['password']
        check = form.cleaned_data['password1']
        if(check != raw_password):
        	return HttpResponse("Check ur password properly bitch")
        user.set_password(raw_password)
        user.save()
        user = authenticate(username=username, password=raw_password)
        if user is not None:
        	if user.is_active:
        		login(request, user)
        		return HttpResponse("Registered u bitch")
        return redirect('signup')

	return render(request, 'signup.html', {"form": form })"""

def logout_view(request):
    logout(request)
    return redirect('/')
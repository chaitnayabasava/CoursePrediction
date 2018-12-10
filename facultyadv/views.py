# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
import smtplib
import MySQLdb
from_="sunil.js16@iiits.in"
pwd="Dark_wolf_jss@6"
db = MySQLdb.connect("localhost","root","manasa@6","ase")

class Dbclass: 
    def __init__(self):
        self.cursor = db.cursor()
    def executeQuery(self,query):
        if self.cursor.execute(query):
            return 1
        else:
            return 0
    def fetch(self,param):
        if param=='1':
            self.result = self.cursor.fetchone()
            if self.result:
                return self.result
            else:
                print "The cursor is empty"
        if param=='*':
            self.result = self.cursor.fetchall()
            if self.result:
                return self.result
            else:
                print "The cursor is empty"

@login_required                
def posts_page(request):
    if request.session['type'] == 'Faculty Advisor':
        cur = Dbclass()
        cur12 = Dbclass()
        faculty = request.session['employee']
        cur2 = Dbclass()
        cur2.executeQuery("select Employee_First_Name from employee where Employee_Reg_No = '"+faculty +"';")
        a = cur2.fetch('*')
        using = str(a[0][0])
        cur12.executeQuery("select distinct s.Student_Id,s.Student_First_Name,s.Student_Middle_Name,s.Student_Last_name,Student_Cur_Sem  from student as s inner join academic_batch as ab on s.Student_Registered_Year = ab.Academic_Batch_Start_Year and s.Student_Registered_Degree = ab.Academic_Batch_Degree inner join faculty_adv_batch as fab on ab.Academic_Batch_Number = fab.batch inner join employee as emp on fab.emp_id = emp.Employee_Id inner join student_sem_course_reg as ssc on s.Student_ID = ssc.Student_Sem_Course_Reg_Student_Id where emp.Employee_Reg_No ="+str(faculty)+" and Student_Sem_Course_Reg_Reg_Status=0;")
        
        cur.executeQuery("select * from posts")

        posts = []
        posts1=[]
        asd = cur12.fetch('*')
        if asd:
            for row1 in asd:
                    if row1!='':
                        posts1.append(row1)
        
        for row in cur.fetch('*'):
                if row!='':
                    posts.append(row)
        
        return render(request, "Facultyadv.html", context={'posts': posts,'posts1':posts1,'using':using})
    else:
        logout(request)
        return redirect('/')           

@login_required
def detail(request,rule_id):
    if request.session['type'] == 'Faculty Advisor':
        cur = Dbclass()
        prompt = ""
        if request.method== "POST":
            prompt = ""
            post = request.POST["editor1"]
            cur.executeQuery("update posts set matter = '" + post + "' where id = "+ rule_id +";")
            db.commit()
            prompt = "Rule " + rule_id + " updated successfully."
        cur.executeQuery("select * from posts where id = " + rule_id + ";")
        d = cur.fetch('*')
        return render(request,"details.html",context={'id': rule_id, 'post_details': d[0][1], 'prompt': prompt})
    else:
        logout(request)
        return redirect('/')           

@login_required
def del_post(   request,rule_id):
    if request.session['type'] == 'Faculty Advisor':
        cur = Dbclass()
        cur.executeQuery("delete from posts where id=" + rule_id + ";")
        db.commit()
        return redirect('/Facultyadv/')
    else:
        logout(request)
        return redirect('/')           

@login_required
def index(request):
    if request.session['type'] == 'Faculty Advisor':
        cur = Dbclass()
        faculty = request.session['employee']
        cur2 = Dbclass()
        cur2.executeQuery("select Employee_First_Name from employee where Employee_Reg_No = '"+faculty +"';")
        a = cur2.fetch('*')
        using = str(a[0][0])
        cur.executeQuery("select distinct s.Student_Id,s.Student_First_Name,s.Student_Middle_Name,s.Student_Last_name,Student_Cur_Sem  from student as s inner join academic_batch as ab on s.Student_Registered_Year = ab.Academic_Batch_Start_Year and s.Student_Registered_Degree = ab.Academic_Batch_Degree inner join faculty_adv_batch as fab on ab.Academic_Batch_Number = fab.batch inner join employee as emp on fab.emp_id = emp.Employee_Id inner join student_sem_course_reg as ssc on s.Student_ID = ssc.Student_Sem_Course_Reg_Student_Id where emp.Employee_Reg_No = '"+ str(faculty)+"' and Student_Sem_Course_Reg_Reg_Status=0")
        a = cur.fetch('*')
        #print(a)
        if a:
    	    a = map(list,a)
    	    #print a
    	    for i in range(len(a)):
        		name = ''
        		if a[i][2]:
        		    name = str(a[i][1]+" "+a[i][2]+" "+a[i][3])
        		else:
        		    name = a[i][1]+" "+a[i][3]
        		a[i][1]=name
        		del a[i][2]
        		del a[i][2]

            cur1 = Dbclass()
            cur1.executeQuery("select Student_Sem_Course_Reg_Batch_Sem_Course from student_sem_course_reg where Student_Sem_Course_Reg_Student_Id="+a[i][0]+";")
            b = cur1.fetch('*')
    		#print b
            courses = []
            s = 0
            for j in b:
                cur2 = Dbclass()
                if cur2.executeQuery("select a.Academic_Prog_Batch_Sem_Course_Credits,ac.Academic_Course_Name from academic_prog_batch_sem_course as a inner join academic_course as ac on a.Academic_Prog_Batch_Sem_Course=ac.Academic_Course_Id where Academic_Course_Id="+str(j[0])+";"):
                    c = cur2.fetch('*')
                    s+=int(c[0][0])
                    courses.append(str(c[0][1])+'-'+str(c[0][0]))
            a[i].append(courses)
            a[i].append(s)        
        return render(request,"applications.html",context = {'courses':a, 'using':using})    
    else:
        logout(request)
        return redirect('/')           

@login_required
def approve(request, student_id):
    if request.session['type'] == 'Faculty Advisor':
        cur = Dbclass()
        #print student_id
        cur.executeQuery("update student_sem_course_reg set Student_Sem_Course_Reg_Reg_Status=1 where Student_Sem_Course_Reg_Student_Id=" + student_id + ";")
        db.commit()
        return redirect("/facultyadv/")
    else:
        logout(request)
        return redirect('/')           

#60010021
@login_required
def disapprove(request,student_id):
    if request.session['type'] == 'Faculty Advisor':
        cur = Dbclass()
        cur10 = Dbclass()
        print("comg")
        if request.method == "POST":
        	print "hello"
    	suggest = request.POST["suggestion"]
    	msg=suggest
    	cur10.executeQuery("select Student_Email from student where Student_ID = '" + student_id + "';")
    	to_= cur10.fetch('*')
    	server = smtplib.SMTP('smtp.gmail.com',587)
    	server.starttls()
    	server.login(from_,pwd)
    	server.sendmail(from_,to_,msg)
    	server.quit()
    	print(suggest)
    	cur.executeQuery("delete from student_sem_course_reg where Student_Sem_Course_Reg_Student_Id='" + student_id + "';")
    	db.commit()
        #print(student_id)
        return redirect("/facultyadv/")

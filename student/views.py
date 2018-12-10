# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import MySQLdb as mysql
from django.contrib.auth import logout
# Create your views here.
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required

now = datetime.datetime.now()
db = mysql.connect("localhost","root","manasa@6","ase")

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
			self.result = self.cursor.aone()
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
def course_poll(request):
	if request.session['type'] == 'Student':
		student_id = request.session['student']
		string = str(now.year)+"-"+str(now.month)+"-"+str(now.day)
		total_credits = 0
		selected_courses = []

		if request.method=="POST":
			cc = request.POST.getlist("cc")
			if cc:
				cur29=db.cursor()
				for i in cc:
					cur29.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur29.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
					
			eb= request.POST.getlist("eb")
			if eb:
				cur28 = db.cursor()
				for i in eb:
					cur28.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur28.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
					
			csb= request.POST.getlist("csb")
			if csb:
				cur30 = db.cursor()
				for i in csb:
					cur30.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur30.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
					
			csc= request.POST.getlist("csc")
			if csc:
				cur31 = db.cursor()
				for i in csc:
					cur31.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur31.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
					
			ec= request.POST.getlist("ec")
			if ec:
				cur32 = db.cursor()
				for i in ec:
					cur32.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur32.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
					
			ie= request.POST.getlist("ie")		
			if ie:
				cur33 = db.cursor()
				for i in ie:
					cur33.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur33.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
					
			me= request.POST.getlist("me")		
			if me:
				cur34 = db.cursor()
				for i in me:
					cur34.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur34.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
					
			se= request.POST.getlist("se")		
			if se:
				cur35 = db.cursor()
				for i in se:
					cur35.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur35.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
					
			h= request.POST.getlist("h")		
			if h:
				cur36 = db.cursor()
				for i in h:
					cur36.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur36.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
							
			ho= request.POST.getlist("ho")		
			if ho:
				cur37 = db.cursor()
				for i in ho:
					cur37.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur37.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
					
			btp= request.POST.getlist("btp")		
			if btp:
				cur38 = db.cursor()
				for i in ho:
					cur38.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur38.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
			#print(selected_courses)
		del_cur = db.cursor()
		del_cur.execute("delete from prediction where Student_Sem_Course_Reg_Student_Id = "+student_id+" and Student_Sem_Course_Reg_Reg_Status = 2;")
		db.commit()
		for i in selected_courses:
			total_credits+=get_credits(i)
			print(get_credits(i))

		if total_credits in range(25, 29):
			#print(total_credits)
			return HttpResponse("If you want to take more than 24 credits please meet the dean and get permission.")
		elif total_credits > 28:
			#print(total_credits)
			return HttpResponse("You cannot opt for more than 28 credits. You may opt for 28 credits onlt with permission of the dean.")
		elif total_credits < 16:
			return HttpResponse("You have to take a minimum credits of 16.")

		if total_credits != 0:
			cur40 = db.cursor()
			cur40.execute("select Student_Sem_Course_Reg_Id from prediction order by Student_Sem_Course_Reg_Id DESC LIMIT 1;")
			var = cur40.fetchall()
			if not var:
				var = 1
			else:
				var = int(var[0][0]) + 1
			cur42 = db.cursor()
			cur42.execute("select Student_Sem_Course_Reg_Batch_Sem_Course from student_sem_course_reg where Student_Sem_Course_Reg_Student_Id ="+student_id+";")
			approved_std = cur42.fetchall()
			approved_std = map(list,approved_std)
			approved_std = reduce(lambda x,y:x+y,approved_std)
			cur43 = db.cursor()
			for i in approved_std:
				if i not in selected_courses:
					cur43.execute("delete from prediction where Student_Sem_Course_Reg_Batch_Sem_Course="+str(i)+" and Student_Sem_Course_Reg_Student_Id="+student_id+";")
					db.commit()
				elif i in selected_courses:
					cur43.execute("insert into prediction values("+str(var)+",'"+student_id+"',"+str(i)+","+str(1)+",'"+string+"',"+"NULL"+","+str(0)+","+"NULL"+");")
					db.commit()
					var+=1
					cur43.execute("delete t1 from prediction as t1 inner join prediction as t2 where t1.Student_Sem_Course_Reg_Id < t2.Student_Sem_Course_Reg_Id and t1.Student_Sem_Course_Reg_Batch_Sem_Course = t2.Student_Sem_Course_Reg_Batch_Sem_Course and t1.Student_Sem_Course_Reg_Reg_Status = t2.Student_Sem_Course_Reg_Reg_Status and t1.Student_Sem_Course_Reg_Student_Id = '"+student_id+"';")
					db.commit()
			for i in selected_courses:
				"""if (i,) in already:
											continue"""
				cur41  = db.cursor()
				cur41.execute("select * from student_sem_course_reg where Student_Sem_Course_Reg_Student_Id='"+student_id+"' and Student_Sem_Course_Reg_Batch_Sem_Course="+str(i)+";")
				if not cur41.fetchall():

					cur40.execute("insert into prediction values("+str(var)+",'"+student_id+"',"+str(i)+","+str(2)+",'"+string+"',"+"NULL"+","+str(0)+","+"NULL"+");")
					db.commit()
					var+=1

		return redirect('/student/course_pred/')
	else:
		logout(request)
		return redirect('/')		   

@login_required
def course_prediction(request):
	if request.session['type'] == 'Student':
		student_id = request.session['student']
		cur2 = Dbclass()
		cur2.executeQuery("select Student_First_Name from student where Student_Id = '"+student_id+"';");
		a = cur2.fetch('*')
		using = a[0][0]

		lll = []
		opted = []
		sss = db.cursor()
		sur = db.cursor()
		sur.execute("select Academic_Prog_Batch_Sem_Course from academic_prog_batch_sem_course where Academic_Prog_Batch_Sem_Course_Sem_Num = (select Student_Cur_Sem from student where Student_Id = '"+student_id+"');")
		already = sur.fetchall()
		who = db.cursor()
		for i in already:
			sss.execute("select Academic_Course_Name from academic_course where Academic_Course_Id ="+str(i[0])+";")
			course = sss.fetchall()[0][0]
			sss.execute("select count(Student_Sem_Course_Reg_Batch_Sem_Course) from prediction where Student_Sem_Course_Reg_Reg_Status in (1,2) and Student_Sem_Course_Reg_Batch_Sem_Course = "+str(i[0])+";")
			count = sss.fetchall()[0][0]
			#print(course)
			sss.execute("select Academic_Prog_Batch_Sem_Course_Credits,Academic_Prog_Batch_Sem_Course_Max from academic_prog_batch_sem_course where Academic_Prog_Batch_Sem_Course ="+str(i[0])+";")
			data = sss.fetchall()
			who.execute("select s.Student_Id,s.Student_First_Name,s.CGPA,s.Student_Registered_Year from student as s inner join prediction as st where s.Student_Id = st.Student_Sem_Course_Reg_Student_Id and st.Student_Sem_Course_Reg_Batch_Sem_Course = "+str(i[0])+" and st.Student_Sem_Course_Reg_Reg_Status != 0 order by  st.Student_Sem_Course_Reg_Reg_Status,s.Student_Registered_Year,s.CGPA desc;")
			#print(who.fetchall()[0])
			a = who.fetchall()
			len_a = len(a)
			counter = 1
			pos = 0
			for j in a:
				if j[0] == student_id:
					pos = counter
				counter+=1
			if pos == 0:
				per = 0
			else:
				per = (1 - (pos/(data[0][1]*1.0)))*100	
			if per<0:
				per = 0					
			print(a)
			print(pos)
			print(len_a)
			opted.append([course, data[0][0], data[0][1], count , per])
			lll.append([course, a])

		print(lll)
		return render(request,"coursePrediction.html",context = {'student_id':student_id, "course":lll, 'opted_by_u':opted, 'using':using})
	else:
		logout(request)
		return redirect('/')

@login_required
def index_student(request):
	if request.session['type'] == 'Student':
		fac=[]
		student_id = request.session['student']
		#print(request.session['type'])
		cur = Dbclass()
		cur1 = Dbclass()
		cur1.executeQuery("select emp.Employee_First_Name,emp.Employee_Second_Name,emp.Employee_Last_Name from student as s inner join academic_batch as ab on s.Student_Registered_Year = ab.Academic_Batch_Start_Year and s.Student_Registered_Degree = ab.Academic_Batch_Degree inner join faculty_adv_batch as fab on ab.Academic_Batch_Number = fab.batch inner join employee as emp on fab.emp_id = emp.Employee_Id where s.Student_ID = 20160010022")
		cur2 = Dbclass()
		cur2.executeQuery("select Student_First_Name from student where Student_Id = '"+student_id+"';");
		a = cur2.fetch('*')
		using = a[0][0]
		for row in cur1.fetch('*'):
			string = ""
			if row[0] and row[0]!="NULL":
				string+= row[0] + " "
			if row[1] and row[1]!="NULL":
				string+= row[1] + " "
			if row[2] and row[2]!="NULL":
				string+= row[2]
			fac.append((string))
		cur.executeQuery("select * from posts")
		posts = []
		for row in cur.fetch('*'):
			posts.append(row)
		std=student_id
			
		return render(request,"index_student.html", context={'posts': posts,'std':std,'fac':fac,'using':using})
	else:
		logout(request)
		return redirect('/')

@login_required
def course_reg(request):
	"""if request.method == "POST":
		course_sel = request.POST.get('course_sel', None)
		print(course_sel)
	cur.execute("select * from dept_type;")
	type_course = []
	for row in cur.fetchall():
		type_course.append(row)

	
	cur1 = db.cursor()
	cur1.execute("select * from academic_prog_batch_sem_course where Academic_Prog_Batch_Sem_Course_Type=1;")
	type_course = []
	for row in cur.fetchall():
		type_course.append(row)
		
	"""
	if request.session['type'] == 'Student':
		student_id = request.session['student']
		common_core = []
		cse_core = []
		ece_core = []
		cse_bouquet = []
		ece_bouquet = []
		IT_Elective = []
		Math_Elective = []
		Science_Elective = []
		humanities = []
		Honors = []
		BTP=[]
		free_electives=[]
		
		sem_no=5
		if sem_no in range(1,4):
			cur = db.cursor()
			cur.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='common core' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			common_core=cur.fetchall()
			common_core = map(list,common_core)
			for i in range(len(common_core)):
				string= ""
				if common_core[i][3]:
					string+=common_core[i][3]+" "
				if common_core[i][4]:
					string+=common_core[i][4]+" "
				if common_core[i][5]:
					string+=common_core[i][5]
				common_core[i].append(string.strip("NULL"))
				del common_core[i][3]
				del common_core[i][3]
				del common_core[i][3]
			
			
		elif sem_no == 4:
			cur1 = db.cursor()
			cur1.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='common core' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			common_core=cur1.fetchall()
			common_core = map(list,common_core)
			for i in range(len(common_core)):
				string= ""
				if common_core[i][3]:
					string+=common_core[i][3]+" "
				if common_core[i][4]:
					string+=common_core[i][4]+" "
				if common_core[i][5]:
					string+=common_core[i][5]
				common_core[i].append(string.strip("NULL"))
				del common_core[i][3]
				del common_core[i][3]
				del common_core[i][3]
			
			
			cur2 = db.cursor()
			cur2.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='cse core' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			cse_core=cur2.fetchall()
			cse_core = map(list,cse_core)
			for i in range(len(cse_core)):
				string= ""
				if cse_core[i][3]:
					string+=cse_core[i][3]+" "
				if cse_core[i][4]:
					string+=cse_core[i][4]+" "
				if cse_core[i][5]:
					string+=cse_core[i][5]
				cse_core[i].append(string.strip("NULL"))
				del cse_core[i][3]
				del cse_core[i][3]
				del cse_core[i][3]
			
			cur3 = db.cursor()
			cur3.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='ece core' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			ece_core=cur3.fetchall()
			ece_core = map(list,ece_core)
			for i in range(len(ece_core)):
				string= ""
				if ece_core[i][3]:
					string+=ece_core[i][3]+" "
				if ece_core[i][4]:
					string+=ece_core[i][4]+" "
				if ece_core[i][5]:
					string+=ece_core[i][5]
				ece_core[i].append(string.strip("NULL"))
				del ece_core[i][3]
				del ece_core[i][3]
				del ece_core[i][3]
					
			
		elif sem_no == 5 or sem_no ==8:
			cur4 = db.cursor()
			cur4.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='common core' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			common_core=cur4.fetchall()
			common_core = map(list,common_core)
			for i in range(len(common_core)):
				string= ""
				if common_core[i][3]:
					string+=common_core[i][3]+" "
				if common_core[i][4]:
					string+=common_core[i][4]+" "
				if common_core[i][5]:
					string+=common_core[i][5]
				common_core[i].append(string.strip("NULL"))
				del common_core[i][3]
				del common_core[i][3]
				del common_core[i][3]
			
			
			cur5 = db.cursor()
			cur5.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='cse core' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			cse_core=cur5.fetchall()
			cse_core = map(list,cse_core)
			for i in range(len(cse_core)):
				string= ""
				if cse_core[i][3]:
					string+=cse_core[i][3]+" "
				if cse_core[i][4]:
					string+=cse_core[i][4]+" "
				if cse_core[i][5]:
					string+=cse_core[i][5]
				cse_core[i].append(string.strip("NULL"))
				del cse_core[i][3]
				del cse_core[i][3]
				del cse_core[i][3]
			
			cur6 = db.cursor()
			cur6.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='ece core' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			ece_core=cur6.fetchall()
			ece_core = map(list,ece_core)
			for i in range(len(ece_core)):
				string= ""
				if ece_core[i][3]:
					string+=ece_core[i][3]+" "
				if ece_core[i][4]:
					string+=ece_core[i][4]+" "
				if ece_core[i][5]:
					string+=ece_core[i][5]
				ece_core[i].append(string.strip("NULL"))
				del ece_core[i][3]
				del ece_core[i][3]
				del ece_core[i][3]
			
			cur7 = db.cursor()
			cur7.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='cse bouquet' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			cse_bouquet=cur7.fetchall()
			cse_bouquet = map(list,cse_bouquet)
			for i in range(len(cse_bouquet)):
				string= ""
				if cse_bouquet[i][3]:
					string+=cse_bouquet[i][3]+" "
				if cse_bouquet[i][4]:
					string+=cse_bouquet[i][4]+" "
				if cse_bouquet[i][5]:
					string+=cse_bouquet[i][5]
				cse_bouquet[i].append(string.strip("NULL"))
				del cse_bouquet[i][3]
				del cse_bouquet[i][3]
				del cse_bouquet[i][3]
			
			cur8 = db.cursor()
			cur8.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='ece bouquet' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			ece_bouquet=cur8.fetchall()
			ece_bouquet = map(list,ece_bouquet)
			for i in range(len(ece_bouquet)):
				string= ""
				if ece_bouquet[i][3]:
					string+=ece_bouquet[i][3]+" "
				if ece_bouquet[i][4]:
					string+=ece_bouquet[i][4]+" "
				if ece_bouquet[i][5]:
					string+=ece_bouquet[i][5]
				ece_bouquet[i].append(string.strip("NULL"))
				del ece_bouquet[i][3]
				del ece_bouquet[i][3]
				del ece_bouquet[i][3]
			
			cur9 = db.cursor()
			cur9.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='IT Elective' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			IT_Elective=cur9.fetchall()
			IT_Elective = map(list,IT_Elective)
			for i in range(len(IT_Elective)):
				string= ""
				if IT_Elective[i][3]:
					string+=IT_Elective[i][3]+" "
				if IT_Elective[i][4]:
					string+=IT_Elective[i][4]+" "
				if IT_Elective[i][5]:
					string+=IT_Elective[i][5]
				IT_Elective[i].append(string.strip("NULL"))
				del IT_Elective[i][3]
				del IT_Elective[i][3]
				del IT_Elective[i][3]
			
			cur10 = db.cursor()
			cur10.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='Math Elective' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			Math_Elective=cur10.fetchall()
			Math_Elective = map(list,Math_Elective)
			for i in range(len(Math_Elective)):
				string= ""
				if Math_Elective[i][3]:
					string+=Math_Elective[i][3]+" "
				if Math_Elective[i][4]:
					string+=Math_Elective[i][4]+" "
				if Math_Elective[i][5]:
					string+=Math_Elective[i][5]
				Math_Elective[i].append(string.strip("NULL"))
				del Math_Elective[i][3]
				del Math_Elective[i][3]
				del Math_Elective[i][3]
			
			cur11 = db.cursor()
			cur11.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='Science Elective' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			Science_Elective=cur11.fetchall()
			Science_Elective = map(list,Science_Elective)
			for i in range(len(Science_Elective)):
				string= ""
				if Science_Elective[i][3]:
					string+=Science_Elective[i][3]+" "
				if Science_Elective[i][4]:
					string+=Science_Elective[i][4]+" "
				if Science_Elective[i][5]:
					string+=Science_Elective[i][5]
				Science_Elective[i].append(string.strip("NULL"))
				del Science_Elective[i][3]
				del Science_Elective[i][3]
				del Science_Elective[i][3]
			
			
			cur12 = db.cursor()
			cur12.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='humanities' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			humanities=cur12.fetchall()
			humanities = map(list,humanities)
			for i in range(len(humanities)):
				string= ""
				if humanities[i][3]:
					string+=humanities[i][3]+" "
				if humanities[i][4]:
					string+=humanities[i][4]+" "
				if humanities[i][5]:
					string+=humanities[i][5]
				humanities[i].append(string.strip("NULL"))
				del humanities[i][3]
				del humanities[i][3]
				del humanities[i][3]
			
			cur13 = db.cursor()
			cur13.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='Honors' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			Honors=cur13.fetchall()
			Honors = map(list,Honors)
			for i in range(len(Honors)):
				string= ""
				if Honors[i][3]:
					string+=Honors[i][3]+" "
				if Honors[i][4]:
					string+=Honors[i][4]+" "
				if Honors[i][5]:
					string+=Honors[i][5]
				Honors[i].append(string.strip("NULL"))
				del Honors[i][3]
				del Honors[i][3]
				del Honors[i][3]
			
			cur14 = db.cursor()
			cur14.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='free electives' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			free_electives=cur14.fetchall()
			free_electives = map(list,free_electives)
			for i in range(len(free_electives)):
				string= ""
				if free_electives[i][3]:
					string+=free_electives[i][3]+" "
				if free_electives[i][4]:
					string+=free_electives[i][4]+" "
				if free_electives[i][5]:
					string+=free_electives[i][5]
				free_electives[i].append(string.strip("NULL"))
				del free_electives[i][3]
				del free_electives[i][3]
				del free_electives[i][3]
			
			
		elif sem_no==6 or sem_no==7:
			cur15 = db.cursor()
			cur15.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='common core' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			common_core=cur15.fetchall()
			common_core = map(list,common_core)
			for i in range(len(common_core)):
				string= ""
				if common_core[i][3]:
					string+=common_core[i][3]+" "
				if common_core[i][4]:
					string+=common_core[i][4]+" "
				if common_core[i][5]:
					string+=common_core[i][5]
				common_core[i].append(string.strip("NULL"))
				del common_core[i][3]
				del common_core[i][3]
				del common_core[i][3]
			
			cur16 = db.cursor()
			cur16.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='cse core' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			cse_core=cur16.fetchall()
			cse_core = map(list,cse_core)
			for i in range(len(cse_core)):
				string= ""
				if cse_core[i][3]:
					string+=cse_core[i][3]+" "
				if cse_core[i][4]:
					string+=cse_core[i][4]+" "
				if cse_core[i][5]:
					string+=cse_core[i][5]
				cse_core[i].append(string.strip("NULL"))
				del cse_core[i][3]
				del cse_core[i][3]
				del cse_core[i][3]
			
			
			cur17 = db.cursor()
			cur17.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='ece core' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			ece_core=cur17.fetchall()
			ece_core = map(list,ece_core)
			for i in range(len(ece_core)):
				string= ""
				if ece_core[i][3]:
					string+=ece_core[i][3]+" "
				if ece_core[i][4]:
					string+=ece_core[i][4]+" "
				if ece_core[i][5]:
					string+=ece_core[i][5]
				ece_core[i].append(string.strip("NULL"))
				del ece_core[i][3]
				del ece_core[i][3]
				del ece_core[i][3]
			
			cur18 = db.cursor()
			cur18.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='cse bouquet' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			cse_bouquet=cur18.fetchall()
			cse_bouquet = map(list,cse_bouquet)
			for i in range(len(cse_bouquet)):
				string= ""
				if cse_bouquet[i][3]:
					string+=cse_bouquet[i][3]+" "
				if cse_bouquet[i][4]:
					string+=cse_bouquet[i][4]+" "
				if cse_bouquet[i][5]:
					string+=cse_bouquet[i][5]
				cse_bouquet[i].append(string.strip("NULL"))
				del cse_bouquet[i][3]
				del cse_bouquet[i][3]
				del cse_bouquet[i][3]
			
			cur19 = db.cursor()
			cur19.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='ece bouquet' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			ece_bouquet=cur19.fetchall()
			ece_bouquet = map(list,ece_bouquet)
			for i in range(len(ece_bouquet)):
				string= ""
				if ece_bouquet[i][3]:
					string+=ece_bouquet[i][3]+" "
				if ece_bouquet[i][4]:
					string+=ece_bouquet[i][4]+" "
				if ece_bouquet[i][5]:
					string+=ece_bouquet[i][5]
				ece_bouquet[i].append(string.strip("NULL"))
				del ece_bouquet[i][3]
				del ece_bouquet[i][3]
				del ece_bouquet[i][3]
			
			cur20 = db.cursor()
			cur20.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='IT Elective' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			IT_Elective=cur20.fetchall()
			IT_Elective = map(list,IT_Elective)
			for i in range(len(IT_Elective)):
				string= ""
				if IT_Elective[i][3]:
					string+=IT_Elective[i][3]+" "
				if IT_Elective[i][4]:
					string+=IT_Elective[i][4]+" "
				if IT_Elective[i][5]:
					string+=IT_Elective[i][5]
				IT_Elective[i].append(string.strip("NULL"))
				del IT_Elective[i][3]
				del IT_Elective[i][3]
				del IT_Elective[i][3]
			
			cur21 = db.cursor()
			cur21.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='Math Elective' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			Math_Elective=cur21.fetchall()
			Math_Elective = map(list,Math_Elective)
			for i in range(len(Math_Elective)):
				string= ""
				if Math_Elective[i][3]:
					string+=Math_Elective[i][3]+" "
				if Math_Elective[i][4]:
					string+=Math_Elective[i][4]+" "
				if Math_Elective[i][5]:
					string+=Math_Elective[i][5]
				Math_Elective[i].append(string.strip("NULL"))
				del Math_Elective[i][3]
				del Math_Elective[i][3]
				del Math_Elective[i][3]
			
			cur22 = db.cursor()
			cur22.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='Science Elective' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			Science_Elective=cur22.fetchall()
			Science_Elective = map(list,Science_Elective)
			for i in range(len(Science_Elective)):
				string= ""
				if Science_Elective[i][3]:
					string+=Science_Elective[i][3]+" "
				if Science_Elective[i][4]:
					string+=Science_Elective[i][4]+" "
				if Science_Elective[i][5]:
					string+=Science_Elective[i][5]
				Science_Elective[i].append(string.strip("NULL"))
				del Science_Elective[i][3]
				del Science_Elective[i][3]
				del Science_Elective[i][3]
			
			cur23 = db.cursor()
			cur23.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='humanities' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			humanities=cur23.fetchall()
			humanities = map(list,humanities)
			for i in range(len(humanities)):
				string= ""
				if humanities[i][3]:
					string+=humanities[i][3]+" "
				if humanities[i][4]:
					string+=humanities[i][4]+" "
				if humanities[i][5]:
					string+=humanities[i][5]
				humanities[i].append(string.strip("NULL"))
				del humanities[i][3]
				del humanities[i][3]
				del humanities[i][3]
			
			cur24 = db.cursor()
			cur24.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='Honors' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			Honors=cur24.fetchall()
			Honors = map(list,Honors)
			for i in range(len(Honors)):
				string= ""
				if Honors[i][3]:
					string+=Honors[i][3]+" "
				if Honors[i][4]:
					string+=Honors[i][4]+" "
				if Honors[i][5]:
					string+=Honors[i][5]
				Honors[i].append(string.strip("NULL"))
				del Honors[i][3]
				del Honors[i][3]
				del Honors[i][3]
			
			cur25 = db.cursor()
			cur25.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='free electives' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			free_electives=cur25.fetchall()
			free_electives = map(list,free_electives)
			for i in range(len(free_electives)):
				string= ""
				if free_electives[i][3]:
					string+=free_electives[i][3]+" "
				if free_electives[i][4]:
					string+=free_electives[i][4]+" "
				if free_electives[i][5]:
					string+=free_electives[i][5]
				free_electives[i].append(string.strip("NULL"))
				del free_electives[i][3]
				del free_electives[i][3]
				del free_electives[i][3]
			
			cur26 = db.cursor()
			cur26.execute("select ac.Academic_Course_Name,dt.name,ap.Academic_Prog_Batch_Sem_Course_Credits,em.Employee_First_Name,em.Employee_Second_Name,em.Employee_Last_Name from academic_prog_batch_sem_course as ap INNER JOIN academic_course as ac ON ac.Academic_Course_Id=ap.Academic_Prog_Batch_Sem_Course INNER JOIN employee AS em ON ap.Academic_Prog_Batch_Sem_Course_Faculty=em.Employee_Id INNER JOIN dept_type as dt ON ap.Academic_Prog_Batch_Sem_Course_Type=dt.id where dt.name='BTP' and ap.Academic_Prog_Batch_Sem_Course_Sem_Num='"+str(sem_no)+"';")
			BTP=cur26.fetchall()
			BTP = list(BTP)
			for i in range(len(BTP)):
				string= ""
				if BTP[i][3]:
					string+=BTP[i][3]+" "
				if BTP[i][4]:
					string+=BTP[i][4]+" "
				if BTP[i][5]:
					string+=BTP[i][5]
				BTP[i].append(string.strip("NULL"))
				del BTP[i][3]
				del BTP[i][3]
				del BTP[i][3]
			
		cur27 = db.cursor()
		cur27.execute("select * from dept_type;")
		type_cour = cur27.fetchall()
		#print common_core

		lll = []
		sss = db.cursor()
		sur = db.cursor()
		sur.execute("select Student_Sem_Course_Reg_Batch_Sem_Course from student_sem_course_reg where Student_Sem_Course_Reg_Student_Id ="+student_id+";")
		already = sur.fetchall()
		sur.execute("select Student_Sem_Course_Reg_Reg_Status from student_sem_course_reg where Student_Sem_Course_Reg_Student_Id=" + student_id + ";")
		approved = sur.fetchall()
		#print(approved[0][0])
		if approved:
			if approved[0][0] == '1':
				approve = "Already approved and so your course registraion is completed. You may now give your polls(NOT MANDATORY)."
			else:
				approve = ""
			print(approve, approved[0][0])
		else:
			approve = ""
		total_credits = 0
		for i in already:
			total_credits+=get_credits(i[0])
			sss.execute("select Academic_Course_Name from academic_course where Academic_Course_Id ="+str(i[0])+";")
			lll.append(sss.fetchall()[0][0])
		print(lll, total_credits)
		cur222 = Dbclass()
		cur222.executeQuery("select Student_First_Name from student where Student_Id = '"+student_id+"';");
		a = cur222.fetch('*')
		using = a[0][0]

		return render(request, "course_registraion.html", context={'total_credits':total_credits, 'student_id':student_id,'type': type_cour, 'common_core': common_core,'cse_core':cse_core,'ece_core':ece_core,'cse_bouquet':cse_bouquet,'ece_bouquet':ece_bouquet,'IT_Elective':IT_Elective,'Math_Elective':Math_Elective,'Science_Elective':Science_Elective,'humanities':humanities,'Honors':Honors,'BTP':BTP,'free_electives':free_electives,'already':lll,'approved':approve,'using':using})
	else:
		logout(request)
		return redirect('/')

def get_credits(course_id):
	cur_common = db.cursor()
	cur_common.execute("select Academic_Prog_Batch_Sem_Course_Credits from academic_prog_batch_sem_course where Academic_Prog_Batch_Sem_Course='"+str(course_id)+"';")
	result = cur_common.fetchall()
	return int(result[0][0])		

@login_required		
def reg_student(request):
	if request.session['type'] == 'Student':
		student_id = request.session['student']
		string = str(now.year)+"-"+str(now.month)+"-"+str(now.day)
		total_credits = 0
		selected_courses = []

		if request.method=="POST":
			cc = request.POST.getlist("cc")
			if cc:
				cur29=db.cursor()
				for i in cc:
					cur29.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur29.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
					
			eb= request.POST.getlist("eb")
			if eb:
				cur28 = db.cursor()
				for i in eb:
					cur28.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur28.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
					
			csb= request.POST.getlist("csb")
			if csb:
				cur30 = db.cursor()
				for i in csb:
					cur30.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur30.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
					
			csc= request.POST.getlist("csc")
			if csc:
				cur31 = db.cursor()
				for i in csc:
					cur31.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur31.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
					
			ec= request.POST.getlist("ec")
			if ec:
				cur32 = db.cursor()
				for i in ec:
					cur32.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur32.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
					
			ie= request.POST.getlist("ie")		
			if ie:
				cur33 = db.cursor()
				for i in ie:
					cur33.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur33.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
					
			me= request.POST.getlist("me")		
			if me:
				cur34 = db.cursor()
				for i in me:
					cur34.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur34.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
					
			se= request.POST.getlist("se")		
			if se:
				cur35 = db.cursor()
				for i in se:
					cur35.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur35.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
					
			h= request.POST.getlist("h")		
			if h:
				cur36 = db.cursor()
				for i in h:
					cur36.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur36.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
							
			ho= request.POST.getlist("ho")		
			if ho:
				cur37 = db.cursor()
				for i in ho:
					cur37.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur37.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])
					
			btp= request.POST.getlist("btp")		
			if btp:
				cur38 = db.cursor()
				for i in ho:
					cur38.execute("select Academic_Course_Id from academic_course where Academic_Course_Name='"+i+"';")
					idd=cur38.fetchone()
					#total_credits+=get_credits(idd[0])
					selected_courses.append(idd[0])

		
		del_cur = db.cursor()
		del_cur.execute("delete from student_sem_course_reg where Student_Sem_Course_Reg_Student_Id = "+student_id+";")
		db.commit()
		for i in selected_courses:
			total_credits+=get_credits(i)
			print(get_credits(i))

		if total_credits in range(25, 29):
			#print(total_credits)
			return HttpResponse("If you want to take more than 24 credits please meet the dean and get permission.")
		elif total_credits > 28:
			#print(total_credits)
			return HttpResponse("You cannot opt for more than 28 credits. You may opt for 28 credits onlt with permission of the dean.")
		elif total_credits < 16:
			return HttpResponse("You have to take a minimum credits of 16.")

		if total_credits != 0:
			cur40 = db.cursor()
			cur40.execute("select Student_Sem_Course_Reg_Id from student_sem_course_reg order by Student_Sem_Course_Reg_Id DESC LIMIT 1;")
			var = cur40.fetchall()
			if not var:
				var = 1
			else:
				var = int(var[0][0]) + 1
			for i in selected_courses:
				"""if (i,) in already:
											continue"""
				cur40.execute("insert into student_sem_course_reg values("+str(var)+",'"+student_id+"',"+str(i)+","+str(0)+",'"+string+"',"+"NULL"+","+str(0)+","+"NULL"+");")
				db.commit()
				var+=1

		return redirect('/student/course_reg/')
	else:
		logout(request)
		return redirect('/')

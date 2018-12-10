# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
import MySQLdb
import datetime

now = datetime.datetime.now()
#db = MySQLdb.connect(host="139.59.25.79",user="admin",passwd="Iiit_s@123",db="ase",)
 
# Create a Cursor object to executeQuery queries.
""" 
# Select data from table using SQL query.
cur.executeQuery("SELECT * FROM examples")
 
# print the first and second columns      
for row in cur.fetch():
    print row[0], " ", row[1]
"""
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

@csrf_exempt
@login_required
def index(request):
	if request.session['type'] == 'Admin':
		cur = Dbclass()
		
		cur.executeQuery("select * from posts")
		posts = []
		for row in cur.fetch('*'):
			posts.append(row)
		
		cur.executeQuery("select a.Academic_Prog_Batch_Sem_Course_Id,ac.Academic_Course_Name,a.Academic_Prog_Batch_Sem_Course_Credits,a.Academic_Prog_Batch_Sem_Course_Sem_Num,d.name,e.Employee_First_Name from academic_prog_batch_sem_course as a inner join academic_course as ac on a.Academic_Prog_Batch_Sem_Course=ac.Academic_Course_Id inner join dept_type as d on a.Academic_Prog_Batch_Sem_Course_Type=d.id inner join employee as e on a.Academic_Prog_Batch_Sem_Course_Faculty=e.Employee_Id  where a.Academic_Prog_Batch_Sem_Course_Curr_Year='"+str(now.year)+"' and Academic_Prog_Batch_Sem_Course_Sem_Num="+str(5)+";")
		catalog = []
		for row in cur.fetch('*'):
			catalog.append(row)

		cur.executeQuery("select f.id,a.Academic_Batch_Start_Year,e.Employee_First_Name,e.Employee_Second_Name,e.Employee_Last_Name from faculty_adv_batch as f inner join academic_batch as a on f.batch=a.Academic_Batch_Id inner join employee as e on f.emp_id=e.Employee_Id;")
		facultyadv = []
		for row in cur.fetch('*'):
			if row[3]:
				facultyadv.append((row[0],row[1],row[2] + " " + row[3] + " " + row[4]  ))
			else:
				facultyadv.append((row[0],row[1],row[2] + " "  + row[4]  ))
		return render(request, "index.html", context={'posts': posts, 'catalog': catalog, 'facultyadv': facultyadv, 'using': 'Admin'})
	else:
		logout(request)
		return redirect("/")	

# ---------------------------------------------------------------------------------------------
@login_required
def posts_page(request):
	if request.session['type'] == 'Admin':
		cur = Dbclass()
		if request.method == "POST":
			rule = request.POST["editor1"]
			print(rule)
			cur.executeQuery("insert into posts (matter) values('"+ rule +"');")
			db.commit()
		cur.executeQuery("select * from posts")
		posts = []
		for row in cur.fetch('*'):
			posts.append(row)
		return render(request, "posts.html", context={'posts': posts, 'using': 'Admin'})
	else:
		logout(request)
		return redirect('/')		   

@login_required
def detail(request,rule_id):
	if request.session['type'] == 'Admin':
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
		return render(request,"details.html",context={'id': rule_id, 'post_details': d[0][1], 'prompt': prompt, 'using': 'Admin'})
	else:
		logout(request)
		return redirect('/')		   

@login_required
def del_post(	request,rule_id):
	if request.session['type'] == 'Admin':
		cur = Dbclass()
		cur.executeQuery("delete from posts where id=" + rule_id + ";")
		db.commit()
		return redirect('/admin_user/')
	else:
		logout(request)
		return redirect('/')		   


# ---------------------------------------------------------------------------------------------
@login_required
def catalog_page(request):
	if request.session['type'] == 'Admin':
		prompt=""
		if request.method == "POST":
			prompt = ""
			course = request.POST["course"]
			credit = request.POST["credit"]
			ug = request.POST["ug"]
			semester = request.POST["semester"]
			type_course = request.POST["type"]
			faculty = request.POST["faculty"]
			maxstr = request.POST["maxstr"] #####################################################################################################
			prompt="Course added to course catalog."

			cur1 = Dbclass()
			cur1.executeQuery("select Academic_Prog_Batch_Sem_Course_Id from academic_prog_batch_sem_course order by Academic_Prog_Batch_Sem_Course_Id DESC LIMIT 1;")
			var = cur1.fetch('*')
			if not var:
				var = '1'
			else:
				var = str(int(var[0][0]) + 1)
			cur11 = Dbclass()
			cur11.executeQuery("insert into academic_prog_batch_sem_course values("+var+","+ug+","+semester+","+course+","+credit+","+str(now.year)+",NULL,NULL,"+type_course+","+faculty+","+maxstr+");")
			db.commit()

		cur = Dbclass()
		cur.executeQuery("select Academic_Batch_Id,Academic_Batch_Start_Year from academic_batch where Strcmp(Academic_Batch_End_Year,'2018')>=0;")
		ugs = []
		for row in cur.fetch('*'):
			ugs.append(row)

		cur3 = Dbclass()
		cur3.executeQuery("select Academic_Course_Id,Academic_Course_Name from academic_course where Academic_Course_Id not in  (select Academic_Prog_Batch_Sem_Course from academic_prog_batch_sem_course);")
		courses = []
		for row in cur3.fetch('*'):
			courses.append(row)

		cur4 = Dbclass()
		cur4.executeQuery("select id,name from dept_type;")
		type_courses = []
		for row in cur4.fetch('*'):
			type_courses.append(row)

		#type_courses = [("core"), ("bore")]
		cur5 = Dbclass()
		cur5.executeQuery("select Employee_Id,Employee_First_Name,Employee_Second_Name,Employee_Last_Name from employee;")
		facultys = []
		for row in cur5.fetch('*'):
			string = ""
			if row[2]:
				if row[1] and row[1]!='NULL':
					string+= row[1] + " "
				if row[2] and row[2]!='NULL':
					string+= row[2] + " "
				if row[3] and row[3]!='NULL':
					string+= row[3]
				facultys.append((row[0],string))
			else:
				if row[1] and row[1]!='NULL':
					string+= row[1] + " "
				if row[3] and row[3]!='NULL':
					string+= row[3]			
				facultys.append((row[0],string))
		#facultys = [("me"), ("he")]

		cur6 = Dbclass()
		cur6.executeQuery("select a.Academic_Prog_Batch_Sem_Course_Id,ac.Academic_Course_Name,a.Academic_Prog_Batch_Sem_Course_Credits,a.Academic_Prog_Batch_Sem_Course_Sem_Num,d.name,e.Employee_First_Name,a.Academic_Prog_Batch_Sem_Course_Max from academic_prog_batch_sem_course as a inner join academic_course as ac on a.Academic_Prog_Batch_Sem_Course=ac.Academic_Course_Id inner join dept_type as d on a.Academic_Prog_Batch_Sem_Course_Type=d.id inner join employee as e on a.Academic_Prog_Batch_Sem_Course_Faculty=e.Employee_Id  where a.Academic_Prog_Batch_Sem_Course_Curr_Year='"+str(now.year)+"';")
		catalog = []
		ass = cur6.fetch('*')
		for row in ass:
			catalog.append(row)
		'''cur66 = db.cursor()
					cur66.execute("select Academic_Prog_Batch_Sem_Course_Max from academic_prog_batch_sem_course;")
					maxe = cur66.fetchall()
					maxx = []
					for row in maxe:
						maxx.append(row)'''
		return render(request, "categories.html", context={'prompt': prompt, 'catalog': catalog, 'ugs': ugs, 'courses': courses, 'types': type_courses, 'facultys': facultys, 'using': 'Admin'})
	else:
		logout(request)
		return redirect('/')		   

@login_required
def course_detail(request,course_id):
	if request.session['type'] == 'Admin':
		cur7 = Dbclass()
		prompt=""
		if request.method== "POST":
			course = request.POST["course"]
			prompt = ""
			credit = request.POST["credits"]
			ug = request.POST["ug"]
			sem = request.POST["sem"]
			type_course = request.POST["type"]
			faculty = request.POST["faculty"]
			maxstr = request.POST["maxstr"] #####################################################################################################
			prompt="Updated details successfully."
			print(type_course)

			cur8 = Dbclass()
			cur8.executeQuery("update academic_prog_batch_sem_course set Academic_Prog_Batch_Sem_Course_Credits="+credit+", Academic_Prog_Batch_Sem_Course_Batch_Id="+ug+",Academic_Prog_Batch_Sem_Course_Sem_Num="+sem+",Academic_Prog_Batch_Sem_Course_Type="+type_course+",Academic_Prog_Batch_Sem_Course_Faculty="+faculty+",Academic_Prog_Batch_Sem_Course_Max="+maxstr+" where Academic_Prog_Batch_Sem_Course_Id ="+course_id+";") 
			
			db.commit()
			print "asdfadsf"


			#cur8.executeQuery("update academic_prog_batch_sem_course set ")

		cur = Dbclass()
		cur.executeQuery("select Academic_Batch_Id,Academic_Batch_Start_Year from academic_batch where Strcmp(Academic_Batch_End_Year,'2018')>=0;")
		ugs = []
		for row in cur.fetch('*'):
			ugs.append(row)


		cur4 = Dbclass()
		cur4.executeQuery("select id,name from dept_type;")
		type_courses = []
		for row in cur4.fetch('*'):
			type_courses.append(row)

		#type_courses = [("core"), ("bore")]
		cur5 = Dbclass()
		cur5.executeQuery("select Employee_Id,Employee_First_Name,Employee_Second_Name,Employee_Last_Name from employee;")
		facultys = []
		for row in cur5.fetch('*'):
			string = ""
			if row[2]:
				if row[1] and row[1]!='NULL':
					string+= row[1] + " "
				if row[2] and row[2]!='NULL':
					string+= row[2] + " "
				if row[3] and row[3]!='NULL':
					string+= row[3]
				facultys.append((row[0],string))
			else:
				if row[1] and row[1]!='NULL':
					string+= row[1] + " "
				if row[3] and row[3]!='NULL':
					string+= row[3]			
				facultys.append((row[0],string))

		cur7.executeQuery("select a.Academic_Prog_Batch_Sem_Course_Id,ac.Academic_Course_Name,a.Academic_Prog_Batch_Sem_Course_Credits,a.Academic_Prog_Batch_Sem_Course_Sem_Num,d.name,e.Employee_First_Name,e.Employee_Second_Name,e.Employee_Last_Name,a.Academic_Prog_Batch_Sem_Course_Max from academic_prog_batch_sem_course as a inner join academic_course as ac on a.Academic_Prog_Batch_Sem_Course=ac.Academic_Course_Id inner join dept_type as d on a.Academic_Prog_Batch_Sem_Course_Type=d.id inner join employee as e on a.Academic_Prog_Batch_Sem_Course_Faculty=e.Employee_Id  where a.Academic_Prog_Batch_Sem_Course_Curr_Year='"+str(now.year)+"' and a.Academic_Prog_Batch_Sem_Course_Id="+course_id+";")
		showdata = cur7.fetch('*')
		print (showdata)
		print("-------------------------------")
		var=""
		if showdata[0][6]:
			if showdata[0][5]:
				var+= showdata[0][5] + " "
			if showdata[0][6]:
				var+= showdata[0][6] + " "
			if showdata[0][7]:
				var+= showdata[0][7]
		else:
			if showdata[0][5]:
				var+= showdata[0][5] + " "
			if showdata[0][7]:
				var+= showdata[0][7]
		#cur.executeQuery("select * from posts where id = " + rule_id + ";")
		#d = cur.fetch()
		return render(request,"course_catalog_details.html",context={"showdata":showdata,"Emp_name":var,"prompt": prompt, 'id': course_id,  'ugs': ugs,  'types': type_courses, 'facultys': facultys, 'using': 'Admin'})
	else:
		logout(request)
		return redirect('/')		   

@login_required
def del_course(request,course_id):
	if request.session['type'] == 'Admin':
		cur = Dbclass()
		cur.executeQuery("delete from academic_prog_batch_sem_course where Academic_Prog_Batch_Sem_Course_Id=" + course_id + ";")
		db.commit()
		return redirect('/admin_user/catalog/')
	else:
		logout(request)
		return redirect('/')		   


# ---------------------------------------------------------------------------------------------
@login_required
def facultyadv_page(request):
	if request.session['type'] == 'Admin':
		prompt=""
		if request.method == "POST":
			prompt=""
			faculty = request.POST["faculty"]
			ug = request.POST["ug"]
			prompt="Facult advisor added successfully."

			cur2 = Dbclass()
			cur2.executeQuery("select id from faculty_adv_batch order by id DESC LIMIT 1;")
			var = cur2.fetch('*')
			if not var:
				var = '1'
			else:	
				var = str(int(var[0][0]) + 1)
			cur1 = Dbclass()
			cur1.executeQuery("insert into faculty_adv_batch values ("+var+ "," + ug + "," + faculty + ");")
			db.commit()

		cur3 = Dbclass()
		cur3.executeQuery("select f.id,a.Academic_Batch_Start_Year,e.Employee_First_Name,e.Employee_Second_Name,e.Employee_Last_Name from faculty_adv_batch as f inner join academic_batch as a on f.batch=a.Academic_Batch_Id inner join employee as e on f.emp_id=e.Employee_Id;")
		facultyadv = []
		for row in cur3.fetch('*'):
			if row[3]:
				facultyadv.append((row[0],row[1],row[2] + " " + row[3] + " " + row[4]  ))
			else:
				facultyadv.append((row[0],row[1],row[2] + " "  + row[4]  ))


		cur = Dbclass()
		cur.executeQuery("select Academic_Batch_Id,Academic_Batch_Start_Year from academic_batch where Strcmp(Academic_Batch_End_Year,'2018')>=0;")
		ug = []
		for row in cur.fetch('*'):
			ug.append(row)


		cur5 = Dbclass()
		cur5.executeQuery("select Employee_Id,Employee_First_Name,Employee_Second_Name,Employee_Last_Name from employee where Employee_Id not in (select emp_id from faculty_adv_batch);")
		faculty = []
		for row in cur5.fetch('*'):
			string=""
			if row[2]:
				if row[1] and row[1]!='NULL':
					string+= row[1] + " "
				if row[2] and row[2]!='NULL':
					string+= row[2] + " "
				if row[3] and row[3]!='NULL':
					string+= row[3]
				faculty.append((row[0],string))
			else:
				if row[1] and row[1]!='NULL':
					string+= row[1] + " "
				if row[3] and row[3]!='NULL':
					string+= row[3]			
				faculty.append((row[0],string))
		#for row in cur.fetch():
		#	catalog.append(row)
		return render(request, "users.html", context={'facultyadv': facultyadv, 'prompt': prompt, 'ugs': ug, 'faculties': faculty, 'using': 'Admin'})
	else:
		logout(request)
		return redirect('/')		   

@login_required
def adv_detail(request, adv_id):
	if request.session['type'] == 'Admin':
		cur = Dbclass()
		prompt=""
		if request.method == "POST":
			prompt=""
			ug = request.POST["ug"]
			prompt="details updated successfully."

			cur11 = Dbclass()
			cur11.executeQuery("update faculty_adv_batch set batch=" +ug+ " where id="+adv_id+";")
			db.commit()


		cur = Dbclass()
		cur.executeQuery("select Academic_Batch_Id,Academic_Batch_Start_Year from academic_batch where Strcmp(Academic_Batch_End_Year,'2018')>=0;")
		ug = []
		for row in cur.fetch('*'):
			ug.append(row)


		cur5 = Dbclass()
		#cur5.executeQuery("select Employee_Id,Employee_First_Name,Employee_Second_Name,Employee_Last_Name from employee where Employee_Id = "+adv_id+";")
		cur5.executeQuery("select e.Employee_Id,e.Employee_First_Name,e.Employee_Second_Name,e.Employee_Last_Name,f.id from faculty_adv_batch as f inner join employee as e on e.Employee_Id=f.emp_id where id = "+adv_id+";")
		faculty = []
		for row in cur5.fetch('*'):
			string=""
			if row[2]:
				if row[1] and row[1]!='NULL':
					string+= row[1] + " "
				if row[2] and row[2]!='NULL':
					string+= row[2] + " "
				if row[3] and row[3]!='NULL':
					string+= row[3]
				faculty.append((row[0],string))
			else:
				if row[1] and row[1]!='NULL':
					string+= row[1] + " "
				if row[3] and row[3]!='NULL':
					string+= row[3]			
				faculty.append((row[0],string))

		faculty = faculty[0][1]
		print(faculty)
		cur6 = Dbclass()
		cur6.executeQuery("select batch from faculty_adv_batch where id="+adv_id+";")
		row = cur6.fetch('*')
		var = str(row[0][0])
		cur66 = Dbclass()
		cur66.executeQuery("select Academic_Batch_Start_Year from academic_batch where Academic_Batch_Id="+var+";")
		row = cur66.fetch('*')
		return render(request, "user_details.html", context={'prompt': prompt, 'ugs': ug, 'faculty': faculty, 'id':adv_id,'year':row[0][0], 'using': 'Admin'})
	else:
		logout(request)
		return redirect('/')		   

@login_required
def adv_del(request, adv_id):
	if request.session['type'] == 'Admin':
		cur = Dbclass()
		cur.executeQuery("delete from faculty_adv_batch where id=" + adv_id + ";")
		db.commit()
		return redirect('/admin_user/facultyadv/')
	else:
		logout(request)
		return redirect('/')		   

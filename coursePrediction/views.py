from __future__ import unicode_literals
import json
import requests
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

def login(request,token):
	res = requests.post(url=' https://serene-wildwood-35121.herokuapp.com/oauth/getDetails', data={
	'token': token,
	'secret': 'bab490cd9c283acf33503df11813fb72f585ab8f99c58a7ddc12a422882bc276f68606341477daa878a5b8379ae73a2305ad668345c5cfacb1e1aa64bd4b7baf'})

	res = json.loads(res.content)
	email = res['student'][0]['Student_Email']
	rollno = res['student'][0]['Student_ID']
	
	if user is not None:
		if user.is_active:
			login(request,user)
			return redirect('/student/' + str(rollno))
	else:
		return render(request, '/', {'status': 'Your account has been disabled'})
		print(email)
	if email:
		return redirect("/facultyadv/")    #print(email)
    
        

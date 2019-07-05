from django.http import HttpResponse
from .models import dept_master,sub_dept,user,book,review,user
from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.models import User


def home(request):
	dept_names= dept_master.objects.all()
	book_names= book.objects.all()
	rev = review.objects.all()
	return render(request,'home.html',	{'dept_names':dept_names,'book_names':book_names,'rev':rev})
#it is link which sends the objects of dept,book and reveiws to the home page for rendering


def requesting(request,user_data):
	if request.method == 'POST':
		user_reg_no = request.POST['user_reg_no']		
		topic = user.objects.create(
			u_name = user_data,
			u_reg_no = user_reg_no
			)
		return redirect('home')
	return render(request,'requesting.html')
# This renders the page requesting the company to giveuser registration number
#and gets the currently logged in user name and creates a user object.


def sub_departments(request, pk):
	
	sub_depts=sub_dept.objects.filter(D_Id=pk)
	dept_name = dept_master.objects.filter(id=pk)
	dept_name = list(dept_name)
	single_dept = dept_name[0]
	return render(request,'sub_dept_list.html',{'sub_depts':sub_depts,'single_dept':single_dept})
#it collects all the sections under a particular dept and sends it the html page for rendering.


def books(request, pk):
	book_list= book.objects.filter(Sub_Id=pk)
	return render(request,'books_list.html',{'book_list':book_list})
#it collects all the books under a particular section and sends it the html page for rendering.


def reviews(request):
	if request.method == 'POST':
		reviewer_name = request.POST['reviewer_name']
		review_description = request.POST['review_description']
		topic = review.objects.create(
			reviewer_name = reviewer_name,
			review_description = review_description
			)
		return redirect('home')
	return render(request,'reviews.html')
#it is a module which takes the reviewer name and its description from the form and make it into a object of review type. 
#after taking reviews it redirects to the home page.


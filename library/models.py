from django.db import models
from django.contrib.auth.models import User

# it is a table which has the department name and image related to that department
class dept_master(models.Model):
	d_name=models.CharField(max_length=30)
	d_image= models.CharField(max_length=50,null=True)
	def __str__(self):
		return (self.d_name)

#it is a table which has the sub dept name and image also it has a forign key from dept_master table which indicate under which dept this comes. 
class sub_dept(models.Model):
	sub_dept_name=models.CharField(max_length=30)
	sub_image= models.CharField(max_length=50,null=True)
	D_Id=models.ForeignKey(dept_master, related_name='department_id', on_delete=models.CASCADE,)
	def __str__(self):
		return (self.sub_dept_name)
		
#it is a table having:
#book name,image,author
#it also has forignkeys from dept_master and sub_dept which helps to track under which dept and sub-dept it belongs. 
class book(models.Model):
	b_name=models.CharField(max_length=100)
	b_author=models.CharField(max_length=30)
	D_Id=models.ForeignKey(dept_master, related_name='department_id1', on_delete=models.CASCADE,)
	Sub_Id=models.ForeignKey(sub_dept, related_name='sub_department_id', on_delete=models.CASCADE,)
	b_image= models.CharField(max_length=50,null=True)
	url=models.URLField(max_length=100,null=True)
	def __str__(self):
		return (self.b_name)

	
#User table to hold the details of user
#every user should have a unique registeration number.
class user(models.Model):
	u_name=models.CharField(max_length=30, null=True)
	u_reg_no=models.CharField(max_length=12, unique=True)
	def __str__(self):
		return (self.u_name)



#Reviews is the table which holds the name of the Reviewer and description about it.
#it is not linked to user/company so that it is anonymous and even admin should not find out.
class review(models.Model):
	reviewer_name = models.CharField(max_length=30, null=True)
	review_description = models.CharField(max_length=250, null=True)
	def __str__(self):
		return (self.review_name)



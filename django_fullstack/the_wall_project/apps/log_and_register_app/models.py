from django.db import models
# from apps.wall_app.models import *

import re	# the regex module
import bcrypt
from datetime import date, datetime,timedelta
today_date = date.today()
another_date= datetime.now()
format_str = '%Y-%m-%d'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')






class UserManager(models.Manager):
    def basic_validator(self, post_data):
       
        PASSWORD_REGEX=re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$')
        if post_data['birthdate'] =="":
            birthdate = datetime.now()
        else:
            birthdate = datetime.strptime(post_data['birthdate'], '%Y-%m-%d')
    
        age = (another_date - birthdate)/365
        required_age = another_date - timedelta(days=13*365)

        errors = {}
# add keys and values to errors dictionary for each invalid field
        for key,value in post_data.items():
            if len(value)==0:
                errors[key]= f"{key} is a required field"
        if len(post_data['first_name']) <2:
            errors['first_name'] = "First name should be atleast 2 character long"
        if len(post_data['last_name']) <2:
            errors['last_name'] = "Last name should be atleast 2 character long"
        # if not PASSWORD_REGEX.match(post_data['password']):
        #     errors['password'] = "Password should be more than 8 character at least one number at least one special character"
        if len(post_data['password']) <2:
            errors['password'] = "Password should be atleast 8 character long"
        if not EMAIL_REGEX.match(post_data['email']): 
            errors['email'] = ("Invalid email address!")
        email_check = User.objects.filter(email = post_data['email'])
        if email_check:
            errors['duplicates'] = "Email already Taken"
        if post_data['password'] != post_data['re_password']:
            errors['not_match'] = "Password and confirm password do not match"
        if post_data['birthdate']:
            if today_date.strftime('%Y-%m-%d') < post_data['birthdate']:
                errors['birthdate_future'] = "That year seams to be in future"
        if str(age) <str(required_age):
            errors['age'] = "you need to be atleast 13 years old"
        return errors
        # if len(post_data['birthdate']) < 1:
        #         errors['birthdate'] = "Please Provide an date and Thank you for your Business"
        #     elif today_date.strftime('%Y-%m-%d') < post_data['birthdate']:
        #         errors['birthdate_future'] = "That year seams to be in future"
        

    def login_validator(self, post_data):
        
        errors = {} # add keys and values to errors dictionary for each invalid field
        for key,value in post_data.items():
            if len(value)==0:
                errors[key]= f"{key} is a required field"
            
            
            existing_user = User.objects.filter(email=post_data['email'])
            if existing_user:
                if bcrypt.checkpw(post_data['password'].encode(), existing_user[0].password.encode()) != True:
                    errors['mismatch'] = "Email and password do not match"
            else:
                errors["not_found"]= "No email found"
            return errors
        


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthdate = models.DateTimeField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()

    
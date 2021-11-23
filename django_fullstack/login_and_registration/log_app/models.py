from django.db import models

import re	# the regex module
import bcrypt
from datetime import date, datetime
today_date = date.today()
another_date= datetime.now()
format_str = '%Y-%m-%d'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        #name validation
        if len(post_data['first_name']) <2:
            errors['first_name'] = "First name should be atleast 2 character long."
        if len(post_data['last_name']) <2:
            errors['last_name'] = "Last name should be atleast 2 character long."
        
        #email validation
        if len(post_data['email']) <1:
            errors['no_email'] = "please provide an email."
        elif not EMAIL_REGEX.match(post_data['email']): 
            errors['email'] = ("Invalid email address!")
        email_check = User.objects.filter(email = post_data['email'])
        if email_check:
            errors['duplicates'] = "Email already Taken."
         #birthdate errors
        if post_data['birthdate'] =="":
            errors['birthdate'] = "Please select a Birthdate"
            
        else:
            birthdate = datetime.strptime(post_data['birthdate'], '%Y-%m-%d')
        if post_data['birthdate']:
                if today_date.strftime('%Y-%m-%d') < post_data['birthdate']:
                    errors['birthdate_future'] = "That year seams to be in future"
        #password validation
        
        if type(post_data['password']) != str:
            errors['not_string']= "Please pass a valid Password."
        symbols = ["!", "@", "#", "$","^", "&", ""]
        if len(post_data['password'])< 8 or len(post_data['password'])>20 or post_data['password'].islower() or post_data['password'].isupper() or post_data['password'].isdigit():
            for symbol in symbols:
                if symbol not in post_data['password']:
                    errors['weak']= "Password should be a mix of Uppercase, lowercase, integer and special charcter and it should be atleast 6 character long."
        elif post_data['password'] != post_data['re_password']:
            errors['not_match'] = "Password and confirm password do not match."
        return errors
        
    def login_validator(self, post_data):
        errors = {} # add keys and values to errors dictionary for each invalid field
        if len(post_data['password']) <1:
            errors['password'] = "Password is a required Field."
        existing_users = User.objects.filter(email=post_data['email'])
        if len(post_data['email']) <1:
            errors['email'] = "Email is a required Field."
        elif len(existing_users) == 0:
            errors["not_found"]= "No email found."
        elif bcrypt.checkpw(post_data['password'].encode(), existing_users[0].password.encode()) != True:
                errors['mismatch'] = "Email and password do not match."
        return errors
        
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthdate = models.DateTimeField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
        

       
        
            
            
    





            
                    


    
        
        
        
       
        


    
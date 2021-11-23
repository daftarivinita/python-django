from django.db import models




# class CourseManager(models.Manager):
#     def basic_validator(self, postData):
#         errors = {}
#         # add keys and values to errors dictionary for each invalid field
#         if len(postData['name']) < 6:
#             errors["name"] = "Course name should be at least 5 characters"
#         if len(postData['description']) <= 15:
#             errors["description"] = "Blog description should be at least 10 characters"
#         return errors
class Course(models.Model):
    name = models.CharField(max_length=45)
    #description = models.OneToOneField(Description, related_name="course",on_delete=models.CASCADE, primary_key=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Description(models.Model):
    content = models.CharField(max_length=255, null = True)  # why we need content here
    course = models.OneToOneField(Course, related_name="description",on_delete=models.CASCADE, primary_key=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #objects = CourseManager() 
# Create your models here.

    #objects = CourseManager() 



class Comment(models.Model): 
    content = models.CharField(max_length=255,null = True)
    course = models.ForeignKey(Course,related_name="has_comments",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


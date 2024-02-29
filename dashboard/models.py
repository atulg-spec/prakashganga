from django.db import models
from django.contrib.auth.models import AbstractUser
from dashboard.manager import *
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_suscribed = models.BooleanField(default=False)
    suscribed_date = models.DateTimeField(auto_now_add=True,null=True)
    expiry_date = models.DateTimeField(default=timezone.now)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25,default='')
    short_description = models.TextField(default="",max_length=150)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

class Chapter(models.Model):
    id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    chapter_number = models.IntegerField()
    chapter_name = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    content = RichTextField()

    def __str__(self):
        return f"Chapter {self.chapter_number}: {self.chapter_name}"

from django.db import models
from django.contrib.auth.models import AbstractUser
from dashboard.manager import *
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_suscribed = models.BooleanField(default=False)
    suscribed_date = models.DateTimeField(auto_now_add=True,null=True)
    expiry_date = models.DateTimeField(default=timezone.now)
    order_id = models.CharField(max_length=100,null=True,blank=True)
    payment_id = models.CharField(max_length=100,null=True,blank=True)
    payment_signature = models.CharField(max_length=100,null=True,blank=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 


class Updates(models.Model):
    subject = models.CharField(max_length=25,default='')
    description = models.TextField(default="",max_length=300)
    def __str__(self):
        return self.subject
    class Meta:
        verbose_name = "Announcement and Update"
        verbose_name_plural = "Announcements and Updates"



class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number_or_email = models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True,blank=True)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us Requests"



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
    thumbnail = models.FileField(upload_to='thumbnail/',null=True,blank=True)
    video = models.FileField(upload_to='videos/')
    content = CKEditor5Field('Text', config_name='extends')

    def __str__(self):
        return f"Chapter {self.chapter_number}: {self.chapter_name}"

from django.db import models
from django.utils import timezone
#from django.views.generic import UpdateView


class Registration(models.Model):
    Student_id = models.AutoField
    Name = models.CharField(max_length=30)
    Registration = models.CharField(max_length=30, primary_key=True)
    Course = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    pswd = models.CharField(max_length=30)
    Gender = models.CharField(max_length=30)

    def __str__(self):
        return self.Name


class Assignment(models.Model):
    Registration = models.CharField(max_length=30)
    Name = models.CharField(max_length=30)
    Course = models.CharField(max_length=50)
    Course_code = models.CharField(max_length=8)
    File = models.FileField(upload_to='dbms/pdf/')
    submit_date = models.DateTimeField(default=timezone.now)
    Project_title = models.CharField(max_length=30, primary_key=True)
    Status = models.CharField(max_length=30, default='Pending')

    def __str__(self):
        return self.Project_title


class Teacher(models.Model):
    Teacher_id = models.CharField(max_length=15)
    pswd = models.CharField(max_length=15)
    Course = models.CharField(max_length=50, default='none')
    Course_code = models.CharField(max_length=8, default='none')

    def __str__(self):
        return self.Teacher_id



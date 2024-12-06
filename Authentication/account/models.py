from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
# Create your models here.

class User(AbstractUser):
  ROLE_CHOICES=(
    ('admin','Admin'),
    ('user','User')
  )
  role=models.CharField(max_length=5,choices=ROLE_CHOICES,default='user')

class Project(models.Model):
  project_name=models.CharField(max_length=1000)
  created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='projects')
  created_at=models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.project_name
    


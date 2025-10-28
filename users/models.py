from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN','Admin'),
        ('TRAINER','Trainer'),
        ('LEARNER','Learner'),
    ]
    
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='LEARNER')
    
    def __str__(self):
        return f"{self.username} ({self.role})"
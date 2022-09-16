from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class UserProfile(models.Model):
    
    name = models.CharField(max_length=16, verbose_name="name of user")
    password = models.CharField(max_length=16, verbose_name="passowrd of user")
    email = models.CharField(max_length=16, verbose_name="email of user")
    job_title = models.CharField(max_length=12, verbose_name="job title of user")
    created_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
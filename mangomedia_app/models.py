from django.db import models
from django.contrib.auth.models import User
#models here.
class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.TextField(max_length=500, blank=True)
   
    def __str__(self):
        return self.user.username


class MangoPost(models.Model):
    author = models.OneToOneField(User,on_delete=models.CASCADE)
    title = models.TextField(max_length=100,blank=False)
    post = models.TextField(max_length=255,blank=False) 
    
    
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime

class User(AbstractUser):
    pass

class Post(models.Model):
    post_text=models.TextField()
    poster=models.ForeignKey(User,on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(User,related_name='blog_post')
    
    class Meta:
        ordering=["-time"]

        
    def __str__(self):
        return self.poster
     
    



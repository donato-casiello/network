from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Comment(models.Model):
    pass 

class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=280)
    n_likes = models.BigIntegerField(default=0)
    #comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    


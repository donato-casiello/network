from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Comment(models.Model):
    pass 

class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_post")
    content = models.TextField(max_length=280)
    #comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.id}: {self.user_id}; content: {self.content}"
    
class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    
    class Meta:
        unique_together = ('user', 'following')
        
    def __str__(self):
        return f"{self.user} follows {self.following}"  

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts")
    
    class Meta:
        unique_together = ('user', 'post')
    
    def __str__(self):
        return f"{self.user} like {self.post}"
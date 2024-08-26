from django.db import models
from django.contrib.auth.models import User
#models here.
class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.TextField(max_length=500, blank=True)
   
    def __str__(self):
        return self.user.username


class MangoPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ManyToManyField(User, related_name='mangoposts')
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(MangoPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
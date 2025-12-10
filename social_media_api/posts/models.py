from django.db import models
from django.contrib.auth import get_user_model

#  Comment should reference both Post (ForeignKey) and User (author), with additional fields for content, created_at, and updated_at.
User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="authors")
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey( User, on_delete=models.CASCADE,related_name="writer")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, related_name='Blogs', on_delete=models.CASCADE)
    post_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.title , self.owner.username)



class Comment(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog , related_name="comments" , on_delete=models.CASCADE)
    post_at = models.DateTimeField(auto_now=True)
    content = models.TextField()


    def __str__(self):
        return '{} - {}'.format(self.blog , self.owner.username)


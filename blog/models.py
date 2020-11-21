from django.db import models
# from django.utils import timezone
from django.urls import reverse
from django.db.models.functions import Now

# Create your models here.

class Post(models.Model):

    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_created = models.DateTimeField(default=Now())
    date_published = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.date_published = Now()
        self.save()

    def published_comments(self):
        return self.comments.filter(published_comment=True)
    
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):

    post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    date_created = models.DateTimeField(default=Now())
    published_comment = models.BooleanField(default=False)

    def publish_comment(self):
        self.published_comment = True
        self.save()
    
    def get_absolute_url(self):
        return reverse('post_list')
    
    def __str__(self):
        return self.text



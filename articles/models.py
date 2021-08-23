from django.db import models
from django.conf import settings # settings ni import qildim
from django.contrib.auth import get_user_model 
from django.urls import reverse


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images/', blank=True, null=True) # blank=True : rasmi yoq maqolalar xatolik bermasligi un
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        )
    blog_view = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])
  
    
class Comment(models.Model):
    post = models.ForeignKey('articles.Article', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        )
    
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
    

    def __str__(self):
        return self.text

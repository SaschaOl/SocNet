from django.db import models
from user_app.models import SocNetUser

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length= 50, null= True)

class Post(models.Model):
    author = models.ForeignKey(SocNetUser, on_delete= models.SET_NULL, null= True)
    title = models.CharField(max_length= 100)
    tags = models.ManyToManyField(Tag, related_name='posts')
    post_text = models.TextField()
    
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name='images')
    file = models.ImageField(upload_to= 'post_images/')


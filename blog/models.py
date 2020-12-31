from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    CATEGORY_CHOICES = [("S", "Science"), ("E", "Engineering"), ("T", "Technology")]
    title = models.CharField(max_length=200)
    username = models.ForeignKey('register.Users', on_delete=models.CASCADE)
    content = RichTextUploadingField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="T")
    def __str__(self):
        return "'" + self.title + "'" + " by user: " + self.username.username + " on " + self.pub_date.strftime("%Y-%m-%d %H:%M:%S")

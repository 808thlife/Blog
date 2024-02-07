from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Post(models.Model):
    date = models.DateField(auto_now_add=True)
    backgroundImage = models.ImageField(upload_to="backgrounds/")
    header = models.CharField(max_length = 254)
    text = RichTextUploadingField()

    def __str__(self):
        return self.header

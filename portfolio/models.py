from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=100,blank=True, null = True )
    sub_content = models.CharField(max_length=100,blank=True, null = True )
    content = RichTextField(blank=True, null = True)
    img = models.ImageField(upload_to= 'asset/intro/pofile/',null=True, blank=True)
    link = models.CharField(max_length=100,blank=True, null = True )
    def __str__(self):
        return self.title
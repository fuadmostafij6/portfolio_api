from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Skill(models.Model):
    icon_name = models.CharField(max_length=100,blank=True, null = True )
    title = models.CharField(max_length=100,blank=True, null = True)
    body = RichTextField(blank=True, null = True)
    img = models.ImageField(upload_to= 'asset/intro/pofile/',null=True, blank=True)

    def __str__(self):
        return self.title

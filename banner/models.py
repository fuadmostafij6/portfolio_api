from django.db import models

# Create your models here.
class Banner(models.Model):
    bg = models.ImageField(upload_to = 'asset/banner/bg/',null=True, blank=True)
    avater = models.ImageField(upload_to = 'asset/banner/avater/',null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    subtitle = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title

class Brand(models.Model):
    image1 = models.ImageField(upload_to= 'asset/banner/barand/',null=True, blank=True)
    image2 = models.ImageField(upload_to= 'asset/banner/barand/',null=True, blank=True)
    image3 = models.ImageField(upload_to= 'asset/banner/barand/',null=True, blank=True)
    image4 = models.ImageField(upload_to= 'asset/banner/barand/',null=True, blank=True)
    image5 = models.ImageField(upload_to= 'asset/banner/barand/',null=True, blank=True)
    image6 = models.ImageField(upload_to= 'asset/banner/barand/',null=True, blank=True)
    image7 = models.ImageField(upload_to= 'asset/banner/barand/',null=True, blank=True)
    image8 = models.ImageField(upload_to= 'asset/banner/barand/',null=True, blank=True)
    image9 = models.ImageField(upload_to= 'asset/banner/barand/',null=True, blank=True)
    
    

    def __str__(self):
        return 'brand'


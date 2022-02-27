from django.db import models

class Nav (models.Model):
    nav = models.CharField(null=True, blank=True, max_length=100)
    brand_image = models.ImageField(upload_to= "asset/mybrand/",null=True, blank=True)
    subtitle = models.CharField(null=True, blank=True, max_length=1000)
    title = models.CharField(null=True, blank=True, max_length=100)


    def __str__(self):
        return self.nav
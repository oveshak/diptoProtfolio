from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.name}"
    
class SocalMedia(models.Model):
    socal_media_name=models.CharField(max_length=20)
    socal_media_url=models.URLField()
    def __str__(self):
        return f"{self.socal_media_name}"


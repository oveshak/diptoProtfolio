from django.db import models
from ckeditor.fields import RichTextField
from solo.models import SingletonModel
# Create your models here.


class HeroItem(SingletonModel):
    names = models.CharField(max_length=30) 
    text = RichTextField(blank=True)
    
    
    def __str__(self):
        return f"{self.names}"

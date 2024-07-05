from django.db import models

# Create your models here.
from solo.models import SingletonModel
# Create your models here.

class BlogItem(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.TextField()
    blog_link= models.URLField()
    
    def __str__(self):
        return self.title


class Blogs(SingletonModel):
    name = models.CharField(max_length=20)
    blog_item = models.ManyToManyField(BlogItem)
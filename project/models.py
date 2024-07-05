from django.db import models

# # Create your models here.


from solo.models import SingletonModel
# Create your models here.

class ProjectItem(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.TextField()
    date=models.DateField()
    language=models.CharField(max_length=100)
    project_url= models.TextField(max_length=50)
    project_link= models.URLField()
    
    def __str__(self):
        return self.title
    
class Projects(SingletonModel):
    name = models.CharField(max_length=20)
    project_item = models.ManyToManyField(ProjectItem)
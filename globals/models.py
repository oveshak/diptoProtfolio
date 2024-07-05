from django.db import models

# Create your models here.
from solo.models import SingletonModel

class Global(SingletonModel):
    footer_text=models.CharField(max_length=100)
    github_link=models.URLField()
    blog_write_side_link=models.URLField()
    project_side_url=models.URLField(blank=True)
    blog_side_url=models.URLField(blank=True)
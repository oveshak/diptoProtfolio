from django.contrib import admin

from project.models import ProjectItem, Projects
from solo.admin import SingletonModelAdmin

# Register your models here.
admin.site.register(ProjectItem)
admin.site.register(Projects,SingletonModelAdmin)
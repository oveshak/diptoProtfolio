from django.contrib import admin

# Register your models here.

from globals.models import Global
from solo.admin import SingletonModelAdmin

admin.site.register(Global,SingletonModelAdmin)
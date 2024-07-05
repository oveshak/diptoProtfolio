from django.contrib import admin

from home.models import HeroItem
from solo.admin import SingletonModelAdmin

# Register your models here.
admin.site.register( HeroItem,SingletonModelAdmin)

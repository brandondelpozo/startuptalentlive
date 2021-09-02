from django.contrib import admin

# Register your models here.

from .models import * # '*'' import all our models

admin.site.register(Talent)

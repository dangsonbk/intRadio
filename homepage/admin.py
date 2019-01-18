from django.contrib import admin
from .models import Letter
from .models import Category
# Register your models here.

admin.site.register(Letter)
admin.site.register(Category)
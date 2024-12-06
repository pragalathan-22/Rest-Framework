from django.contrib import admin
from .models import Category, Service

# Register the models for admin interface
admin.site.register(Category)
admin.site.register(Service)

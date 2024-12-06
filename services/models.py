from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return self.name

class Service(models.Model):
    category = models.ForeignKey(Category, related_name='services', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='service_images/')
    description = models.TextField()

    def __str__(self):
        return self.name

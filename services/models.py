from django.db import models

# Create your models here.
class Offers(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="uploads")
    price = models.IntegerField()
    hours = models.IntegerField(default=0)
    rating = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name
    
    
class Employee(models.Model):
    name = models.CharField(max_length=50)
    detail = models.TextField()
    image = models.ImageField(upload_to="uploads")
    PhoneNumber = models.IntegerField()
    
    def __str__(self):
        return self.name

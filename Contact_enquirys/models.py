from django.db import models
from accounts.models import Account
from services.models import Offers

class ContactEnquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    comments = models.TextField()
    job_salary = models.IntegerField()

class Review(models.Model):
    service = models.ForeignKey(Offers, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=50, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

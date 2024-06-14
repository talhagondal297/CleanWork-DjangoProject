
from django import forms
from .models import Review


class CustomerReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['subject', 'review', 'rating']


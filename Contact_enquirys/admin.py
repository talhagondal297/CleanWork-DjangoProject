from django.contrib import admin
from Contact_enquirys.models import ContactEnquiry
from .models import Review
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job_salary', 'comments')

admin.site.register(ContactEnquiry, ContactAdmin)
admin.site.register(Review)

from sqlite3 import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from Contact_enquirys.forms import CustomerReviewForm
from Contact_enquirys.models import ContactEnquiry
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from services.models import Offers
from .models import Review



# Create your views here.
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        job_salary = request.POST.get("job-salary")
        comments = request.POST.get("message")
        
        try:
            ContactData = ContactEnquiry(name=name, email=email, job_salary=job_salary, comments=comments)
            ContactData.save()
            # Optional: Success message ya success page par redirect kar sakte hain.
        except IntegrityError as e:
            print("Data save karne mein error:", e)
            # Error ko theek tareeke se handle karein (jaise user ko error message dikhana).
        
    return render(request, "contact.html")


# from .forms import CustomerReviewForm  # Create a form for handling input

@login_required(login_url="login")
def reviews(request, service_id):
    url = request.META.get('HTTP_REFERER')
    if url is None:
        url = '/'  # Default URL if HTTP_REFERER is None

    service = get_object_or_404(Offers, id=service_id)
    if request.method == "POST":
        try:
            reviews = Review.objects.get(user__id=request.user.id, service__id=service_id)
            form = CustomerReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except Review.DoesNotExist:
            form = CustomerReviewForm(request.POST)
            if form.is_valid():
                data = Review()
                data.user = request.user  # Set the user field
                data.service = service  # Set the service field
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get("REMOTE_ADDR")

                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)
    return redirect(url)
from django.shortcuts import get_object_or_404, render
from services.models import Offers, Employee
from Contact_enquirys.models import Review
from django.db.models import Avg

def index(request):
    offers = Offers.objects.all()
    reviews = Review.objects.all().order_by("-rating")[:9]
    data = {
        'reviews':reviews,
        'offers': offers,
    }
    return render(request, 'index.html', data)


def about(request):
    employeedata = Employee.objects.all()
    context = {
        'employeedata':employeedata,
    }
    return render(request, 'about.html', context)


def coming_soon(request):
    return render(request, 'coming_soon.html')


def contact(request):
    return render(request, 'contact.html')


def services_detail(request, service_id):
    service = get_object_or_404(Offers, id=service_id)
    reviews = Review.objects.filter(service=service)
    total_reviews = reviews.count()
    average_review = reviews.aggregate(Avg('rating'))['rating__avg'] or 0

    context = {
        'service': service,
        'reviews': reviews,
        'total_reviews': total_reviews,
        'average_review': average_review,
    }
    return render(request, 'services_detail.html', context)


def page_404(request):
    return render(request, 'page_404.html')


def services(request):
    service = list(Offers.objects.all())
    context = {
        'service':service,
    }
    return render(request, 'services.html', context)

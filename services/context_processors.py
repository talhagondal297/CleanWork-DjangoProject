from .models import Offers


def Service(request):
    try:
        services = Offers.objects.all()
    except Exception as e:
        print(e) 
    
    return dict(services=services)

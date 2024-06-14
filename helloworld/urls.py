
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include("accounts.urls")),
    path('Contact_enquirys/',include("Contact_enquirys.urls")),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    path('coming_soon/', views.coming_soon, name='coming_soon'),
    path('services_detail/<int:service_id>/', views.services_detail, name='services_detail'),
    path('page_404/', views.page_404, name='page_404'),
    path('services/', views.services, name='services'),
    
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)


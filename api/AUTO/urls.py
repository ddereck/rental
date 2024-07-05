"""
URL configuration for AUTO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('api/', views.home),
    path('api/', include('Car.urls')),
    path('api/', include('Discount.urls')),
    path('api/', include('Inventory.urls')),
    path('api/', include('Maintenance.urls')),
    path('api/', include('Notification.urls')),
    path('api/', include('Rental.urls')),
    path('api/', include('Review.urls')),
    path('api/', include('Search.urls')),
    path('api/', include('StatReport.urls')),
    path('api/', include('Transaction.urls')),
    path('api/', include('User.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
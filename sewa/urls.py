"""
URL configuration for sewa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from catalog.views import home, send_order, about, calculator_page, post_calculator_page
from django.conf import settings
from django.conf.urls.static import static
from feedback.views import feedback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('send_order/', send_order, name='send-order'),
    path('about/', about, name='about'),
    path('feedback/', feedback, name='feedback'),
    path('calculator_page/', calculator_page, name='calculator_page'),
    path('calc_price/', post_calculator_page, name='calc_price')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
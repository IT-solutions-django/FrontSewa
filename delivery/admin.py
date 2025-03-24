from django.contrib import admin
from .models import Delivery, City, DeliveryBody

admin.site.register(DeliveryBody)
admin.site.register(Delivery)
admin.site.register(City)

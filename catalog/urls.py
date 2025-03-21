from django.urls import path
from catalog.views import catalog, car, get_models_from_api

app_name = 'catalog'

urlpatterns = [
    path('korea/', catalog, name='korea'),
    path('car/<int:id_car>/', car, name='car'),
    path('get-models/', get_models_from_api, name='get-models')
]

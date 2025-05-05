from django.urls import path
from catalog.views import catalog, car, get_models_from_api, get_promo_car_card, get_insurance, get_inspection

app_name = 'catalog'

urlpatterns = [
    path('korea/', catalog, {'country': 'Корея'}, name='korea'),
    path('japan/', catalog, {'country': 'Япония'}, name='japan'),
    path('china/', catalog, {'country': 'Китай'}, name='china'),
    path('europe/', catalog, {'country': 'Европа'}, name='europe'),
    path('car/<int:id_car>/', car, name='car'),
    path('get-models/', get_models_from_api, name='get-models'),
    path('promo_car/<int:id_car>/', get_promo_car_card, name='promo-car'),
    path('car_insurance/', get_insurance, name='car_insurance'),
    path('car_inspection/', get_inspection, name='car_inspection'),
]

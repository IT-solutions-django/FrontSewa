from django import forms


ENGINE_TYPE_CHOICES = [
    ('Бензин', 'Бензиновый'),
    ('Дизель', 'Дизельный'),
    ('Гибрид', 'Гибрид'),
    ('Электро', 'Электрический'),
]

AGE_CHOICES = [
    ('<3', 'меньше 3-х лет'),
    ('3-5', 'от 3 до 5 лет'),
    ('>5', 'более 5 лет'),
]


class CalculatorForm(forms.Form):
    vehicle_price = forms.DecimalField(
        label='Стоимость авто (в валюте)',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'padding: 12px; border-radius: 16px;'})
    )

    manufacture_year = forms.ChoiceField(
        label='Год выпуска',
        choices=AGE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'padding: 12px; border-radius: 16px;'})
    )

    engine_volume = forms.IntegerField(
        label='Объем двигателя, см³',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'padding: 12px; border-radius: 16px;'})
    )

    engine_power = forms.IntegerField(
        label='Мощность двигателя, л.с.',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'padding: 12px; border-radius: 16px;'})
    )

    engine_type = forms.ChoiceField(
        label='Тип двигателя',
        choices=ENGINE_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'padding: 12px; border-radius: 16px;'})
    )





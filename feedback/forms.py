from django import forms
from django.core.validators import RegexValidator
from .models import FeedBack


class FeedBackForm(forms.ModelForm):
    phone = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^(\+7|7|8)?[\s\-]?\(?[0-9]{3}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
                message="Введите корректный российский номер телефона"
            )
        ]
    )

    class Meta:
        model = FeedBack
        fields = ['name', 'phone', 'message', 'city_delivery']


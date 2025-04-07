from django.shortcuts import render
import json
from django.views.decorators.http import require_POST
from .forms import FeedBackForm
from django.http import JsonResponse


@require_POST
def feedback(request):
    data = json.loads(request.body)

    form = FeedBackForm(data)

    if form.is_valid():
        feedback_form = form.save()
        return JsonResponse({
            'status': 'success',
            'id': feedback_form.id
        }, status=201)
    else:
        return JsonResponse({
            'status': 'error',
            'errors': form.errors
        }, status=400)


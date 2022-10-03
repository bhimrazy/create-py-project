from django.http import JsonResponse
from http import HTTPStatus


def index(request):
    return JsonResponse({'message': "Welcome to Django REST framework API"}, content_type='application/json', status=HTTPStatus.OK)

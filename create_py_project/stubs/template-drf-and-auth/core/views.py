from http import HTTPStatus

from django.http import JsonResponse


def index(request):
    return JsonResponse(
        {"message": "Welcome to Django REST framework API"},
        content_type="application/json",
        status=HTTPStatus.OK,
    )

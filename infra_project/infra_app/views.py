from urllib import response

from django.http import HttpResponse


def index(request):
    return HttpResponse(HttpResponse, 'У меня получилось!')


def second_page(request):
    return HttpResponse(HttpResponse, 'А это вторая страница')

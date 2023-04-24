from django.shortcuts import render
from django.http import HttpResponse


def order_view(request, url):
    return HttpResponse(request, f'{url}')

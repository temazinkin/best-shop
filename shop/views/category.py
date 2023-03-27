from django.shortcuts import render
from django.http import HttpResponse


def category_view(request, url):
    return HttpResponse(request, f'{url}')

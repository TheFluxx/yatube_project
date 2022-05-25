from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница')

def group_posts(request):
    return HttpResponse('Посты, отфильтрованные по группам')

def group_number(request, pk):
    return HttpResponse(f'Пост номер {pk}')
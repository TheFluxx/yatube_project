from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    template = 'posts/index.html'

    title = 'Это главная страница проекта Yatube'

    context = {
        'title': title
    }
    return render(request, template, context) 

def group_posts(request):
    list_group = 'posts/group_list.html'

    title = 'Здесь будет публиковаться информация о группах проекта Yatube'

    context = {
        'title': title
    }
    return render(request, list_group, context)

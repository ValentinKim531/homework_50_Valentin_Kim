from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from random import randint

from webapp.views.cat import Cat


def add_view(request: WSGIRequest):
    if request.method == "GET":
        print(request.GET)
        text = (request.GET.get('text'))
        context = {'text': text, 'age': Cat.age, 'happyness_level': Cat.happyness_level, 'satiety': Cat.satiety}
        return render(request, 'article_create.html', context=context)
    print(request.POST)
    context = {'text': request.GET.get('text'), 'age': Cat.age, 'happyness_level': Cat.happyness_level, 'satiety': Cat.satiety}

    if request.POST.get('action') == 'play':
        if Cat.status == "sleep":
            Cat.status = "woken_up"
            Cat.happyness_level -= 5
        elif Cat.status == "woken_up":
            rage_probability = randint(1, 100)
            if rage_probability <= 33:
                Cat.happyness_level = 0
            else:
                Cat.happyness_level += 15
            Cat.satiety -= 10

    elif request.POST.get('action') == 'feed':
        if Cat.status != "sleep":
            Cat.satiety += 15
            if Cat.satiety > 100:
                Cat.happyness_level -= 30
            Cat.happyness_level += 5

    elif request.POST.get('action') == 'sleep':
        Cat.status = 'sleep'
        print(Cat.status)

    return redirect('/cat_stats', context=context)


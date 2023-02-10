from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.cat import Cat

cat = Cat()


def index_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == "POST":
        cat.name = request.POST.get('name', 'unnamed')
        return render(request, 'cat_stats.html', context={
            'name': cat.name,
            'health': cat.health,
            'happiness': cat.happiness,
            'satiety': cat.satiety,
            'rage': cat.rage
        })


def stats(request: WSGIRequest):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'play':
            cat.play()
        elif action == 'feed':
            cat.feed()
        elif action == 'sleep':
            cat.sleep()

        return render(request, 'cat_stats.html', context={
            'name': cat.name,
            'health': cat.health,
            'happiness': cat.happiness,
            'satiety': cat.satiety,
            'rage': cat.rage,
            'state': cat.state
        })

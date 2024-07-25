from django.shortcuts import render

from goods.models import Categories 

def index(request):

    
    context = {
        'title': 'Аленкафе-Главное',
        'content': 'Интрига в каждой чашке',
    }
    return render(request, 'main/index.html',context)


def about(request):
    context = {
        'title': 'Аленкафе-О нас',
        'content': 'О нас',
        'text_on_page':'даддадададададад'
    }
    return render(request, 'main/about.html',context)
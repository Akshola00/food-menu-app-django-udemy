from django.shortcuts import render
from django.http import HttpResponse
from food.models import Item
from django.template import loader
# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {
        "item_list":item_list,
    }
    template = loader.get_template('food/index.html')
    return HttpResponse(template.render(context, request))

def item(request):
    return HttpResponse('<h1>this is an item view</h1>')


def detail(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {
        "item":item
    }
    return render(request, 'food/details.html', context)
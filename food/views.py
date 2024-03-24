from django.shortcuts import redirect, render
from django.http import HttpResponse
from food.models import Item
from django.template import loader
from .forms import itemform
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

def create_item(request):
    form = itemform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, 'food/item-form.html', context={'form':form})

def update_food(request, id):
    item = Item.objects.get(id=id)
    form = itemform(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('/food')
    
    return render(request, 'food/item-form.html', context={'form':form, 'item':item})

def delete(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect("/food")
    return render(request, 'food/confirm_delete.html', context = {'item':item})
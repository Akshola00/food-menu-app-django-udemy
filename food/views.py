from django.forms import BaseModelForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from food.models import Item
from django.template import loader
from .forms import itemform
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


class index(ListView):
    model = Item;
    template_name = 'food/index.html'
    context_object_name = 'item_list'


class detail(DetailView):
    model = Item;
    template_name = 'food/details.html'



class create_item(CreateView):
    model = Item;
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'
    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)


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
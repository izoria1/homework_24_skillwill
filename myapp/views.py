from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item
from django.urls import reverse_lazy

class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'

class ItemCreateView(CreateView):
    model = Item
    template_name = 'item_form.html'
    fields = ['name', 'description']

class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'item_form.html'
    fields = ['name', 'description']

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_confirm_delete.html'
    success_url = reverse_lazy('item_list')

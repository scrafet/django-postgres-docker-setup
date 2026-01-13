from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Item
from .forms import ItemForm

# Reusable Mixins

class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

class SuccessMessageMixin:
    success_message = ""

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.success_message:
            messages.success(self.request, self.success_message)
        return response

class BaseListView(LoginRequiredMixin, TitleMixin, ListView):
    """
    Base view for listing items with DataTables support.
    """
    pass

class BaseCreateView(LoginRequiredMixin, TitleMixin, SuccessMessageMixin, CreateView):
    """
    Base view for creating items.
    """
    template_name = 'core/form.html'

class BaseUpdateView(LoginRequiredMixin, TitleMixin, SuccessMessageMixin, UpdateView):
    """
    Base view for updating items.
    """
    template_name = 'core/form.html'

class BaseDeleteView(LoginRequiredMixin, DeleteView):
    """
    Base view for deleting items.
    """
    template_name = 'core/confirm_delete.html'
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Item deleted successfully.")
        return super().delete(request, *args, **kwargs)

# Concrete Views for Item

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

class ItemListView(BaseListView):
    model = Item
    template_name = 'core/item_list.html'
    context_object_name = 'items'
    title = 'Item List'

class ItemCreateView(BaseCreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('item_list')
    success_message = "Item created successfully!"
    title = 'Create Item'

class ItemUpdateView(BaseUpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('item_list')
    success_message = "Item updated successfully!"
    title = 'Edit Item'

class ItemDeleteView(BaseDeleteView):
    model = Item
    success_url = reverse_lazy('item_list')

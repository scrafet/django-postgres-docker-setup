from django.urls import path
from .views import (
    CustomLoginView,
    ItemListView,
    ItemCreateView,
    ItemUpdateView,
    ItemDeleteView
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', ItemListView.as_view(), name='item_list'),
    path('add/', ItemCreateView.as_view(), name='item_add'),
    path('item/<int:pk>/edit/', ItemUpdateView.as_view(), name='item_edit'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
]

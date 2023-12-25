from django.urls import path
from .views import ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    path('', ItemListView.as_view(), name='item_list'),
    path('<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('new/', ItemCreateView.as_view(), name='item_new'),
    path('<int:pk>/edit/', ItemUpdateView.as_view(), name='item_edit'),
    path('<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
]

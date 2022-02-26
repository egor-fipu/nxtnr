from django.urls import path

from .views import NewOrder, OrdersList

urlpatterns = [
    path('', NewOrder.as_view(), name='new_order'),
    path('list/', OrdersList.as_view(), name='orders_list'),
]

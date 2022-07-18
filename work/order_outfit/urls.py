from django.urls import path

from . import views

app_name = 'order_outfit'

urlpatterns = [
    path('order_outfit_all/', views.order_outfit_all, name='order_all'),
    path('order_outfit_detail/<int:order_id>/', views.order_outfit_detail, name='order_detail'),
    path('order_outfit_create/', views.order_outfit_create, name='order_create')
]

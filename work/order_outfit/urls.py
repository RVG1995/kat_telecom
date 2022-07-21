from django.urls import path

from . import views

app_name = 'order_outfit'

urlpatterns = [
    path('all/', views.order_outfit_all, name='order_all'),
    path('detail/<int:order_id>/', views.order_outfit_detail, name='order_detail'),
    path('create/', views.order_outfit_create, name='order_create')
]

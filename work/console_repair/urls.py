from django.urls import path

from . import views

app_name = 'console_repair'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.console_repair_create, name='create'),
    path('console_repair/<int:repair_id>',
         views.console_repair_detail, name='detail'),
    path('console_repair_all/', views.console_repair_all, name='all')
]

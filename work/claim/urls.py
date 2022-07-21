from django.urls import path

from . import views

app_name = 'claim'

urlpatterns = [
    path('all/', views.claim_all, name='claim_all'),
    # path('detail/<int:claim_id>/', name='claim_detail'),
    path('create/', views.claim_create, name='claim_create'),
    path('update/<claim_id>/edit', views.claim_edit, name='claim_update')
]

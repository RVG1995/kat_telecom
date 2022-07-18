from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import OrderOutfitForm
from .models import OrderOutfit


def order_outfit_all(request):
    order = OrderOutfit.objects.all()
    context = {
        'order': order,
    }

    return render(request, 'order_outfit/order_outfit_all.html', context)


def order_outfit_detail(request, order_id):
    order = get_object_or_404(OrderOutfit, id=order_id)
    context = {
        'order': order,
    }

    return render(request, 'order_outfit/order_outfit_detail.html', context)


def order_outfit_create(request):
    form = OrderOutfitForm(request.POST)
    if form.is_valid():
        order = form.save()
        return redirect('order_outfit:order_detail', order_id=order.id)
    context = {
        'form': form,
    }
    return render(request, 'order_outfit/order_outfit_form.html', context)

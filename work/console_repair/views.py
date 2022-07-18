from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import RepairForm
from .models import Repair


def index(request):
    repair = Repair.objects.all()
    context = {
        'console': repair
    }
    return render(request, 'console_repair/index.html', context)


def console_repair_all(request):
    repair = Repair.objects.all()
    context = {
        'repairs': repair,
    }
    return render(request, 'console_repair/console_repair_all.html', context)


def console_repair_detail(request, repair_id):
    console = get_object_or_404(Repair, id=repair_id)
    context = {
        'repair': console,
    }
    return render(
        request,
        'console_repair/console_repair_detail.html',
        context)


def console_repair_create(request):
    form = RepairForm(request.POST)
    if form.is_valid():
        repair = form.save()
        return redirect('console_repair:detail', repair_id=repair.id)
    context = {
        'form': form,
    }
    return render(request, 'console_repair/console_repair_form.html', context)

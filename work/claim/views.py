from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import ClaimForm
from .models import Claim


def claim_all(request):
    claim = Claim.objects.all()
    context = {
        'claims': claim,
    }
    return render(request, 'claim/claim_all.html', context)


def claim_detail(request, claim_id):
    claim = get_object_or_404(Claim, id=claim_id)
    context = {
        'claim': claim,
    }
    return render(
        request,
        'claim/claim_detail.html',
        context)


def claim_create(request):
    form = ClaimForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('claim:claim_all')

    context = {
        'form': form,
    }
    return render(request, 'claim/claim_form.html', context)


def claim_edit(request, claim_id):
    claim = get_object_or_404(Claim, id=claim_id)
    form = ClaimForm(request.POST or None,
                     instance=claim)

    if form.is_valid():
        form.save()
        return redirect("claim:claim_all")

    form = ClaimForm(instance=claim)

    context = {"form": form,
               "claim": claim,
               }
    return render(request, "claim/claim_update.html", context)

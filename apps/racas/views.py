from django.shortcuts import render, get_object_or_404, redirect
from .forms import RacaForm
from .models import Raca

# Create your views here.

def add_raca(request):
    template_name = 'racas/add_raca.html'
    context = {}
    if request.method == 'POST':
        form = RacaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('racas:list_racas')
    form = RacaForm()
    context['form'] = form
    return render(request, template_name, context)

def list_racas(request):
    template_name = 'racas/list_racas.html'
    racas = Raca.objects.filter()
    context = {
        'racas': racas
    }
    return render(request, template_name, context)

def edit_raca(request, id_raca):
    template_name = 'racas/add_raca.html'
    context ={}
    raca = get_object_or_404(Raca, id=id_raca)
    if request.method == 'POST':
        form = RacaForm(request.POST, instance=raca)
        if form.is_valid():
            form.save()
            return redirect('racas:list_racas')
    form = RacaForm(instance=raca)
    context['form'] = form
    return render(request, template_name, context)

def delete_raca(request, id_raca):
    raca = Raca.objects.get(id=id_raca)
    raca.delete()
    return redirect('racas:list_racas')
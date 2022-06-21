from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ConsultaForm
from .models import Consulta
from .models import Consulta, Raca, ConsultaRaca

# Create your views here.

def add_consulta(request):
    template_name = 'consulta/add_consulta.html'
    context = {}
    if request.method == 'POST':
        form = ConsultaForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('consulta:sucess_consulta')
    form = ConsultaForm()
    context['form'] = form
    return render(request, template_name, context)

def list_consultas(request):
    template_name = 'consulta/list_consultas.html'
    consulta_racas = ConsultaRaca.objects.filter()
    racas = Raca.objects.filter()
    consultas = Consulta.objects.filter()
    context = {
        'consultas': consultas,
        'racas': racas,
        'consulta_racas': consulta_racas
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_consulta(request, id_consulta):
    template_name = 'consulta/add_consulta.html'
    context ={}
    consulta = get_object_or_404(Consulta, id=id_consulta)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('consulta:list_consultas')
    form = ConsultaForm(instance=consulta)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_consulta(request, id_consulta):
    consulta = Consulta.objects.get(id=id_consulta)
    consulta.delete()
    return redirect('consulta:list_consultas')


def sucess_consulta(request):
    template_name = 'consulta/sucess_consulta.html'
    context = {}
    return render(request, template_name, context)
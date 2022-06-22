from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Internacao
from .forms import InternacaoForm

# Create your views here.

@login_required(login_url='/contas/login/')
def add_internacao(request):
    template_name = 'internacao/add_internacao.html'
    context = {}
    if request.method == 'POST':
        form = InternacaoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('internacao:list_internacoes')
    form = InternacaoForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
def list_internacoes(request):
    template_name = 'internacao/list_internacoes.html'
    internacoes = Internacao.objects.filter()
    context = {
        'internacoes': internacoes
    }
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
def edit_internacao(request, id_internacao):
    template_name = 'internacao/add_internacao.html'
    context ={}
    internacao = get_object_or_404(Internacao, id=id_internacao)
    if request.method == 'POST':
        form = InternacaoForm(request.POST, request.FILES,  instance=internacao)
        if form.is_valid():
            form.save()
            return redirect('internacoes:list_internacoes')
    form = InternacaoForm(instance=internacao)
    context['form'] = form
    return render(request, template_name, context)

def delete_internacao(request, id_internacao):
    internacao = Internacao.objects.get(id=id_internacao)
    internacao.delete()
    return redirect('internacoes:list_internacoes')
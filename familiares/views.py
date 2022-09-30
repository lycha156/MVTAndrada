from django.shortcuts import render, redirect, get_object_or_404
from .models import Familiar
from .forms import FamiliarForm
from django.contrib import messages
from django.db.models import Q

def index(request):
    if request.method == 'POST':
        query = request.POST['q']
        familiares = Familiar.objects.filter( Q(nombre__contains = query) | Q(apellido__contains = query) | Q(direccion__contains = query) | Q(email__contains = query) | Q(telefono__contains = query) | Q(dni__contains = query) )
    else:
        familiares = Familiar.objects.all()[:50]

    context = {
        'familiares': familiares
    }
    return render(request, 'familiares_index.html', context)


def create(request):
    form = FamiliarForm()
    if request.method == 'POST':
        form = FamiliarForm(request.POST)

        try:
            if form.is_valid():
                resultado = form.save()
                messages.success(request, 'Familiar guardado con exito.')
                # return redirect('socios_show', resultado.id)
                return redirect('familiares_index')
            else:
                messages.warning(request, 'Error durante la carga de los datos')
                return render(request, 'familiares_create.html', context = {'form': form})
        except Exception as e:
            messages.warning(request, f'Error al realizar la carga de datos. {e}')
            return redirect('familiares_index')

    context = {
        'form': form
    }
    return render(request, 'familiares_create.html', context)

def update(request, id=id):
    obj = get_object_or_404(Familiar, pk=id)
    form = FamiliarForm(request.POST or None, instance=obj)

    if form.is_valid():
        try:
            form.save()
            messages.success(request, 'Familiar actualizado con exito.-')
            return redirect('familiares_index')
        except Exception as e:
            messages.warning(request, f'Error al actualizar. {e}')
            return redirect('familiares_index')

    context = {
        'form': form
    }
    return render(request, 'familiares_create.html', context)

def show(request, id=id):
    familiar = get_object_or_404(Familiar, pk=id)

    context = {
        'familiar': familiar
    }
    return render(request, 'familiares_show.html', context)

def delete(request, id=id):
    familiar = get_object_or_404(Familiar, pk=id)

    if request.method == 'POST':
        try:
            familiar.delete()
            messages.success(request, 'Los datos del familiar fueron eliminados con exito.-')
            return redirect('familiares_index')
        except Exception as e:
            messages.warning(request, f'Error al eliminar los datos. {e}')
            return redirect('familiares_index')

    context = {
        'familiar': familiar
    }
    return render(request, 'familiares_delete.html', context)
    


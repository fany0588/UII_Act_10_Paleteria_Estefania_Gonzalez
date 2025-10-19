from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def index(request):
    return render(request, 'app_producto/index.html', {
        'productos': Producto.objects.all()
    })

def ver_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    return HttpResponseRedirect(reverse('index'))


def add(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            new_nombre = form.cleaned_data['nombre']
            new_descripcion = form.cleaned_data['descripcion']
            new_precio = form.cleaned_data['precio']
            new_stock = form.cleaned_data['stock']
            new_categoria = form.cleaned_data['categoria']
            new_id_ingrediente = form.cleaned_data['id_ingrediente']

        nuevo_producto = Producto(
            nombre=new_nombre,
            descripcion=new_descripcion,
            precio=new_precio,
            stock=new_stock,
            categoria=new_categoria,
            id_ingrediente=new_id_ingrediente
        )

        nuevo_producto.save()
        return render(request, 'app_producto/add.html', {
            'form': ProductoForm(),
            'success': True
        })
    else:
        form = ProductoForm()
    return render(request, 'app_producto/add.html', {
        'form': ProductoForm()
    })

from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm

# Editar un producto existente
def edit_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    success = False

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            success = True
            return redirect('index')  # Redirige al index después de guardar
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'app_producto/edit.html', {
        'form': form,
        'producto': producto,
        'success': success
    })

def delete(request, producto_id):
    if request.method == 'POST':
        producto = Producto.objects.get(pk=producto_id)
        producto.delete()
    return HttpResponseRedirect(reverse('index'))
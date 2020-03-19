from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User,Group
from .models import mega_juego,cate_Jueg,requisitos_completos
from django.core.paginator import Paginator
from django.views.defaults import page_not_found
from django.http import Http404
# Create your views here.
def mi_error_404(request,exception):
    return page_not_found(request,exception,template_name="404.html")

#def sitemap(request):
#        return render(request,"sitemap.xml",content_type="application/xhtml+xml")   
def principal(request):
    categorias=cate_Jueg.objects.get_queryset().order_by('id')
    productos=mega_juego.objects.get_queryset().order_by('id')
    paginator=Paginator(productos,30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data={
        'page_obj':page_obj,
        'categorias':categorias,
    }
    return render(request,"principal.html",data)
def juego(request, slug):
    categorias=cate_Jueg.objects.get_queryset().order_by('id')
    #productos=mega_juego.objects.filter(slug=slug)
    productos=get_object_or_404(mega_juego, slug=slug)
    data={
        'productos':productos,
        'categorias':categorias,
    }
    return render(request,"Juego.html",data)
def categoria(request,slug):
    categorias=cate_Jueg.objects.get_queryset().order_by('id')
    juegos=mega_juego.objects.filter(categoria_pro__slug2=slug)
    if juegos.exists():
        paginator=Paginator(juegos,30)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data={
            'page_obj':page_obj,
            'categorias':categorias,    
        }
        return render(request,"Categoria.html",data)
    else:
        return redirect('principal')

def anio(request,anio_estreno):
    categorias=cate_Jueg.objects.get_queryset().order_by('id')
    productos=mega_juego.objects.filter(anio_estreno=anio_estreno)
    if productos.exists():
        paginator=Paginator(productos,30)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data={
            'page_obj':page_obj,
            'categorias':categorias,
        }
        return render(request,"anio.html",data)
    else:
        return redirect('principal')

def requisitos(request,requisitos):
    categorias=cate_Jueg.objects.get_queryset().order_by('id')
    productos=mega_juego.objects.filter(requisitos=requisitos)
    if productos.exists():
        paginator=Paginator(productos,30)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data={
            'page_obj':page_obj,
            'categorias':categorias,
        }
        return render(request,"requisitos.html",data)
    else:
        return redirect('principal')
        
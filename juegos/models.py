from datetime import date, datetime
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django_matplotlib import MatplotlibFigureField
from django.urls import reverse
# Create your models here.

YEARS=[]
for r in range(1980, (datetime.now().year+1)):
    YEARS.append((r,r))
REQUISITOS=(
    ("Requisitos Bajos","Requisitos Bajos"),
    ("Requisitos Medios","Requisitos Medios"),
    ("Requisitos Altos","Requisitos Altos"),
)
class User(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    edad=models.IntegerField()
    imagen=models.ImageField()
    
    def __str__(self):
        return self.nombre
class requisitos_completos(models.Model):
    CPU=models.CharField(max_length=150)
    RAM=models.CharField(max_length=150)
    Targeta_Grafica=models.CharField(max_length=150)
    SO=models.CharField(max_length=50)
    Memoria_disk=models.CharField(max_length=100)
    CPU_recomendado=models.CharField(max_length=150,null=True,blank=True)
    RAM_recomendado=models.CharField(max_length=15,null=True,blank=True)
    Targeta_Grafica_recomendado=models.CharField(max_length=150,null=True,blank=True)
    SO_recomendado=models.CharField(max_length=50,null=True,blank=True)
    Memoria_disk_recomendado=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.CPU,self.RAM,self.Memoria_disk
class cate_Jueg(models.Model):
    nombre=models.CharField(max_length=100)
    slug2=models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.nombre
def slug_generator(sender,instance,*args,**kwargs):
    if instance.slug2:
        return
    instance.slug2=slugify(instance.nombre)
pre_save.connect(slug_generator,sender=cate_Jueg)
class cate_serv(models.Model):
    nombre=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
class mega_juego(models.Model):
        nombre=models.CharField(max_length=150,verbose_name="Nombre")
        nom_abre=models.CharField(max_length=100,verbose_name="Nombre Abreviado")
        fecha_registro=models.DateField(verbose_name="Fecha Registro")
        descripcion=models.CharField(max_length=500,verbose_name="Descripcion")
        descri_abre=models.CharField(max_length=100,verbose_name="Descripcion Abreviada")
        anio_estreno=models.IntegerField(max_length=4, choices=YEARS,verbose_name="Año de Estreno",null=True, blank=True,default=datetime.now().year)
        requisitos=models.CharField(max_length=50,verbose_name="Requisitos",null=True, blank=True,choices=REQUISITOS,default=REQUISITOS[0])
        requisitos_completo=models.ForeignKey(requisitos_completos,on_delete=models.CASCADE,verbose_name="Requisitos Completos",null=True,blank=True)
        enlacegd=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive")
        enlacegd2=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive 2")
        enlacegd3=models.CharField(max_length=250,blank=True,verbose_name="Enlace Google Drive 3")
        enlacemg=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega ")
        enlacemg2=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega 2")
        enlacemg3=models.CharField(max_length=250,blank=True,verbose_name="Enlace Mega 3")
        enlace_publi=models.CharField(max_length=250,blank=True,verbose_name="Enlace con Publicidad Google Drive 1")
        enlace_publi2=models.CharField(max_length=250,blank=True,verbose_name="Enlace con Publicidad Google Drive 2")
        enlace_publi3=models.CharField(max_length=250,blank=True,verbose_name="Enlace con Publicidad Google Drive 3")
        enlace_publimg=models.CharField(max_length=250,blank=True,verbose_name="Enlace con Publicidad Mega 1")
        enlace_publimg2=models.CharField(max_length=250,blank=True,verbose_name="Enlace con Publicidad Mega 2")
        enlace_publimg3=models.CharField(max_length=250,blank=True,verbose_name="Enlace con Publicidad Mega 3")
        categoria_pro=models.ManyToManyField(cate_Jueg,verbose_name="Categoria Producto")
        slug=models.SlugField(null=True,blank=True)
        imagen=models.ImageField()
        imagen2=models.ImageField()
        imagen3=models.ImageField()
        def __str__(self):
            return self.nombre
def slug_generator2(sender,instance,*args,**kwargs):
    if instance.slug:
        return
    instance.slug=slugify(instance.nombre)
pre_save.connect(slug_generator,sender=mega_juego)
             
class servi_juego(models.Model):
    nombre=models.CharField(max_length=150)
    nom_abre=models.CharField(max_length=100)
    fecha_registro=models.DateField()
    pre_servi=models.FloatField()
    categoria_ser=models.ForeignKey(cate_serv,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
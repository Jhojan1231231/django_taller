from django.contrib import admin
from .models import cliente, reparacion

admin.site.register(cliente)
class clienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'direccion')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('nombre', 'apellido')
    
admin.site.register(reparacion)
class reparacionAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'descripcion', 'fecha_ingreso', 'fecha_entrega', 'estado')
    search_fields = ('cliente__nombre', 'cliente__apellido', 'descripcion')
    list_filter = ('estado', 'fecha_ingreso', 'fecha_entrega')

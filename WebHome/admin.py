from django.contrib import admin
from .models import Proveedor, Sitios, Tipo_enlace, Reclamos

admin.site.register(Sitios)
admin.site.register(Reclamos)
admin.site.register(Proveedor)
admin.site.register(Tipo_enlace)



from django.contrib import admin
from administrar.models import Tarea


class TareaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "estado", "desc")

    def desc(self, obj):
        if obj.estado:
            return 'Completado'
        else:
            return 'Pendiente'


admin.site.register(Tarea, TareaAdmin)

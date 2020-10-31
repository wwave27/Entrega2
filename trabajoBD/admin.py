from django.contrib import admin
from trabajoBD.models import Usuario, Noticia, Lanzamientos, Reviews, Tags
# Register your models here.

#class ContentAdmin(admin.ModelAdmin):
#    readonly_fields=("created", "update")

admin.site.register(Usuario)
admin.site.register(Noticia)
admin.site.register(Lanzamientos)
admin.site.register(Reviews)
admin.site.register(Tags)
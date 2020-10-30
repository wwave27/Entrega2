from django.contrib import admin
from trabajoBD.models import Usuario, Noticia, Lanzamientos, Reviews
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["titulo","subtitulo"]
    search_fields = ["titulo"]

admin.site.register(Usuario)
admin.site.register(Noticia)
admin.site.register(Lanzamientos)
admin.site.register(Reviews)
from django.contrib import admin
from jerarquia import models


@admin.register(models.Categoría)
class CategoríaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)


@admin.register(models.JerarquíaCategorías)
class JerarquíaCategoríasAdmin(admin.ModelAdmin):
    list_display = ("superior_categoría_id", "inferior_categoría_id")


@admin.register(models.Objeto)
class ObjetoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoría_superior_id")


@admin.register(models.ComposiciónObjeto)
class ComposiciónObjetoAdmin(admin.ModelAdmin):
    list_display = ("objeto_id", "categoría", "descripción")
    list_filter = ("objeto_id",)

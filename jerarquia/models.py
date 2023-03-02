from django.db import models


class Categoría(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.nombre}"


class JerarquíaCategorías(models.Model):
    superior_categoría_id = models.ForeignKey(Categoría, on_delete=models.CASCADE, related_name="sup")
    inferior_categoría_id = models.ForeignKey(Categoría, on_delete=models.CASCADE, related_name="inf")

    class Meta:
        verbose_name = "jerarquía de categoría"
        verbose_name_plural = "jerarquía de categorías"

    def __str__(self) -> str:
        return f"{self.superior_categoría_id} - {self.inferior_categoría_id}"


class Objeto(models.Model):
    categoría_superior_id = models.ForeignKey(JerarquíaCategorías, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.categoría_superior_id}"


class ComposiciónObjeto(models.Model):
    objeto_id = models.ForeignKey(Objeto, on_delete=models.CASCADE)
    categoría = models.ForeignKey(JerarquíaCategorías, on_delete=models.CASCADE, related_name="comp_sup")
    descripción = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.objeto_id} - {self.categoría} {self.descripción}"

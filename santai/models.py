from django.db import models


class Order(models.Model):
    is_permitted = models.BooleanField(verbose_name="Разрешенный?", default=False)
    name = models.CharField(verbose_name="Имя", max_length=255, blank=False)
    phone = models.CharField(verbose_name="Телефон", max_length=255, blank=False)
    updated_at = models.DateTimeField("Дата начала", blank=True, auto_now=True)

    class Meta:
        verbose_name = "Звонок"
        verbose_name_plural = "Звоноки"
        ordering = ["-updated_at"]

    def __str__(self):
        return f"{self.name} {self.phone}"

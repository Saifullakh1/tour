from django.db import models


class Tour(models.Model):
    class Currency(models.TextChoices):
        som = "som"
        dollar = "dollar"
        euro = "euro"
    title = models.CharField(
        max_length=250, verbose_name="Название"
    )
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="tour_images", verbose_name="Картинка"
    )
    price = models.IntegerField(
        default=0, verbose_name="Цена"
    )
    currency = models.CharField(
        max_length=100, choices=Currency.choices,
        default=Currency.som, verbose_name="Валюта"
    )
    created_at = models.DateField(
        auto_created=True, verbose_name="Дата создания"
    )
    is_active = models.BooleanField(
        default=True, verbose_name="Активный"
    )

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"

    def __str__(self):
        return self.title


from django.db import models


class Guide(models.Model):
    name = models.CharField(
        max_length=250, verbose_name="Имя"
    )
    title = models.CharField(
        max_length=250, verbose_name="Должность"
    )
    image = models.ImageField(
        upload_to="guides_images", verbose_name="Картинка"
    )
    facebook = models.CharField(
        max_length=250, blank=True, verbose_name="Facebook"
    )
    twitter = models.CharField(
        max_length=250, blank=True, verbose_name="Твиттер"
    )
    instagram = models.CharField(
        max_length=250, blank=True, verbose_name="Инстаграм"
    )
    is_active = models.BooleanField(
        default=True, verbose_name="Активный"
    )

    class Meta:
        verbose_name = "Гид"
        verbose_name_plural = "Гиды"

    def __str__(self):
        return self.name
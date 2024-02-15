from django.db import models


class Review(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Имя"
    )
    city = models.CharField(
        max_length=150, verbose_name="Город"
    )
    image = models.ImageField(
        upload_to="review_images", verbose_name="Фото"
    )
    text = models.CharField(
        max_length=250, verbose_name="Текст"
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.name

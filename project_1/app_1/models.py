from django.db import models


class Mebel(models.Model):
    link = models.TextField('Ссылка')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(
        'Описание с Куфара'
    )
    parse_datetime = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        verbose_name='Дата добавления'
    )

    def get_absolute_url(self):  # добавляет кнопку 'открыть на сайте' и переходит по ссылке
        return self.link

    def __str__(self):
        return f"{self.price} | {self.description[:20]}"

    class Meta:
        verbose_name = 'Мебель'
        verbose_name_plural = 'Мебель'
        ordering = ['-price']

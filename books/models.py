import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Заголовок", max_length=200)
    author = models.CharField("Автор", max_length=200)
    price = models.DecimalField("Цена", max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Review(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="reviews", verbose_name="Книга"
    )
    review = models.CharField("Отзыв", max_length=255)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, verbose_name="Автор"
    )

    def __str__(self):
        return self.review

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

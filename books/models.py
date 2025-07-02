import uuid
from django.db import models
from django.urls import reverse


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

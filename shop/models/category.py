from django.db.models import (
    Model,
    CharField,
    SlugField,
)
from django.urls import reverse


class Category(Model):
    title = CharField(
        'название',
        max_length=200,
    )
    url = SlugField(
        'URL',
        unique=True,
    )

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse(
            'category',
            kwargs={
                'url': self.url,
            }
        )

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'
        db_table = 'categories'

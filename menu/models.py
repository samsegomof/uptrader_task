from django.db import models


class MenuElement(models.Model):
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField('url', max_length=100)
    parent = models.ForeignKey('self', verbose_name='Родительская категория',
                               on_delete=models.CASCADE, null=True, blank=True,
                               related_name='children')

    def __str__(self):
        return self.name

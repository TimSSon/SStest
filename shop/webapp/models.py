from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse


class Category(MPTTModel):
    name = models.CharField(verbose_name=_("Название"),
                            max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey('self', verbose_name=_("Родитель"), on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    def get_absolute_url(self):
        if self.parent_id:
            return reverse(
                'subcategory',
                kwargs={'category': self.parent.slug,
                        'subcategory': self.slug}
            )
        else:
            return reverse('category', kwargs={'subcategory': self.slug})

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

# Create your models here.


class Item(models.Model):
    name = models.CharField(
        max_length=40, verbose_name=_("Название"), db_index=True)
    description = models.CharField(max_length=250, verbose_name=_("Описание"))
    price = models.PositiveIntegerField(verbose_name=_('Цена'))
    category = models.ForeignKey(
        "webapp.Category", verbose_name=_("Категория"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

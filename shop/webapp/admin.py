from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter
from .models import Category, Item


class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title','slug',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('name',), }

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Item,
            'category',
            'products_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                                                Item,
                                                'category',
                                                'products_count',
                                                cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Кол-во продуктов (для этой категории)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Кол-во продуктов (в подкатегориях)'


class ItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'price')
    list_display_links = ('pk', 'name')
    list_filter = ('category', TreeRelatedFieldListFilter),
    search_fields = ('name',)



admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)

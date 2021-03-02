from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import ListView, DetailView
from webapp.models import Category, Item
from django.utils import timezone
from mptt.exceptions import InvalidMove
from django.urls import reverse
from django.db.models import Q
import mptt

# Create your views here.


def index(request):
    return render(request, ('base.html'))


class IndexView(ListView):
    model = Item
    context_object_name = 'data'
    template_name = 'webapp/index_view.html'

    def get_queryset(self):
        queryset = {'items': Item.objects.all(),
                    'category': Category._default_manager.all()}
        return queryset

class CategoryListView(ListView):
    model = Item
    context_object_name = 'data'
    template_name = 'webapp/index_view.html'

    def get_queryset(self):
        queryset = {'items': Item.objects.filter(category_id=self.kwargs.get('pk')),
                    'category': Category.objects.all()}
        return queryset

        # queryset = {'items': Item.objects.filter(category_id=self.kwargs.get('pk')),
        #             'category': Category.objects.all()}
        # return queryset

from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import ListView, DetailView
from webapp.models import Category, Item
from django.core.paginator import Paginator, PageNotAnInteger
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q
import mptt

# Create your views here.


def index(request):
    return render(request, ('base.html'))


class IndexView(ListView):
    model = Item
    template_name = 'webapp/index_view.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = Item.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        items = self.get_queryset()
        paginator = Paginator(items, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        context = {'items': items,
                   'category': Category.objects.all()
                   }
        return context


class CategoryListView(ListView):
    model = Item
    template_name = 'webapp/index_view.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = Item.objects.filter(Q(category__slug=self.kwargs.get(
            'subcategory')) | Q(category__parent__slug=self.kwargs.get('subcategory')))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        items = self.get_queryset().order_by('id')
        paginator = Paginator(items, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        context = {'items': items,
                   'category': Category.objects.all()
                   }
        return context

    # queryset = {'items': Item.objects.filter(category_id=self.kwargs.get('pk')),
    #             'category': Category.objects.all()}
    # return queryset

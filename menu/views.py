from django.db.models import Q
from django.shortcuts import render
from django.views import View

from menu.models import MenuElement


class MenuDetailView(View):
    """Display all nested categories with children of chosen category"""
    def get(self, request, slug):
        query_path = slug.split('/')
        queryset = MenuElement.objects.select_related('parent').filter(
            Q(parent=None) | Q(parent__slug__in=query_path))
        return render(request, 'main.html', {'categories': queryset,
                                             'category_path': query_path[0],
                                             'query_path': query_path,
                                             })


class MenuView(View):
    """Display only root categories without parents"""
    def get(self, request):
        return render(request, 'main.html', {
            'categories': MenuElement.objects.select_related('parent').filter(
                parent=None), })

from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category, Page


def index(request):
    cate = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': cate}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    return render(request, 'rango/about.html')


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        page = Page.objects.filter(category=category)
        context_dict['pages'] = page
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None

    return render(request, 'rango/category.html', context_dict)


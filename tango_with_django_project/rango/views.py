from django.shortcuts import render
from .models import Category, Page
from django.http import HttpResponse

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    # print('Categorias: ', len(category_list), ':', category_list)
    page_list = Page.objects.order_by('-views')[:5]

    print('Páginas: ', len(page_list), ':', page_list)

    context_dict = {'categories':category_list, 'pages':page_list}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'autor': 'Ana e Bruno'}
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    # print(context_dict)
    # return HttpResponse(context_dict)
    return render(request, 'rango/category.html', context_dict)
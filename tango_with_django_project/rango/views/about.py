from django.shortcuts import render


def about(request):
    context_dict = {'autor': 'Marco André Mendes'}
    return render(request, 'rango/about.html', context=context_dict)
from django.shortcuts import render


def about(request):
    context_dict = {'autor': 'Ana e Bruno'}
    return render(request, 'rango/about.html', context=context_dict)

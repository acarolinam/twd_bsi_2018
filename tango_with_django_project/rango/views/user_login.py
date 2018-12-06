from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Sua conta no Rango está desabilitada.")
        else:
            print("Detalhes de login inválidos: {0}, {1}".format(username, password))
            return HttpResponse("Detalhes de login inválido fornecidos.")
    else:
        return render(request, 'rango/login.html', {})
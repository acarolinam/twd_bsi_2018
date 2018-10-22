from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View

from .login_required import LoginRequiredMixin
from ..forms import CategoryForm


class Add_Category(LoginRequiredMixin, View):
    form_class = CategoryForm
    initial = {}
    template_name = 'rango/add_category.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('index'))

        return render(request, self.template_name, {'form': form})
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from ..forms import PageForm
from ..models import Category

class Add_Page(View):
    form_class = PageForm
    initial = {}
    template_name = 'rango/add_page.html'

    def get(self, request, category_name_slug=None):
        try:
            category = Category.objects.get(slug=category_name_slug)
        except Category.DoesNotExist:
            category = None

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'category':category})

    def post(self, request,  category_name_slug=None):
        try:
            category = Category.objects.get(slug=category_name_slug)
        except Category.DoesNotExist:
            category = None

        form = self.form_class(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return HttpResponseRedirect(reverse('show_category', args=(category_name_slug,)))

        return render(request, self.template_name, {'form': form, 'category':category})
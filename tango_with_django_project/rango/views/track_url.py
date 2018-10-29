from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from ..models import Page


def track_url(request, page_id):
    url = reverse('index')
    try:
        page = Page.objects.get(id=page_id)
        print(page.url, page.views)
        page.views += 1
        page.save()
        url = page.url
    except Page.DoesNotExist:
        print("Não achou: %s" %page_id)

    return redirect(url)
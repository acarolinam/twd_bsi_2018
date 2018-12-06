from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

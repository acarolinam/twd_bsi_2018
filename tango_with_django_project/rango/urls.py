from django.conf.urls import url
from . import views
from .views import Add_Category, Add_Page


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^restricted/', views.restricted, name='restricted'),

    url(r'^register/', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),

    url(r'^like/$', views.like_category, name='like_category'),

    url(r'^goto/(?P<page_id>[0-9]+)/$', views.track_url, name='goto'),

    url(r'^add_category/', Add_Category.as_view(), name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
    url(r'^(?P<category_name_slug>[\w\-]+)/add_page/$',
        Add_Page.as_view(), name='add_page'),
]

#!/usr/bin/env python3

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    categories = open('populate_rango_categories.csv').readlines()
    print('Populating %d categories...' %len(categories))
    for categorie in categories:
        cat = categorie.strip()
        c = add_cat(cat)
    pages = open('populate_rango_pages.csv').readlines()
    print('Populating %d pages...' %len(pages))
    for page in pages:
        cat, title, url, views = page.strip().split(',')
        c = add_cat(cat)
        ok = add_page(c, title, url, views)


def show():
    # Print out the categories we have added.
    print('Showing pages...')
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

# Start execution here!


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
    show()

from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
            return self.name


class Page(models.Model):
    categoria = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def _str_(self):
        return self.title

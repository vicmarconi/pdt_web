from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    author = models.TextField()

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = 'articles'

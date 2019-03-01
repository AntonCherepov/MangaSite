from django.db import models


class Main(models.Model):
    """Модель для новостей"""
    text = models.TextField('Text', max_length=500)
    pub_date = models.DateTimeField('date published', auto_now_add=True)


class User:
    pass

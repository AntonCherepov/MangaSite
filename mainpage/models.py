from django.db import models


class Main(models.Model):
    """Модель для новостей"""
    text = models.TextField('Text', max_length=500)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    main_image = models.ImageField('Image_name')


class User(models.Model):
    pass


class Files(models.Model):
    pass

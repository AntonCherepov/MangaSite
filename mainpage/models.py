from django.contrib.auth.models import User
from django.db.models import (ImageField, DateTimeField, TextField,
                              FileField, CharField, ForeignKey,
                              BooleanField, Model, PositiveIntegerField,
                              ManyToManyField, CASCADE, IntegerField)


class Project(Model):
    """ Модель хранения информации о проекте"""

    name = CharField(max_length=100)
    description = TextField(max_length=1000, default="")
    author = CharField(max_length=50, default="Не указан")
    genres = CharField(max_length=100, default="Не указаны")
    # active, dropped, finished, maybe
    status = CharField(max_length=8, null=True)
    staff_name = ManyToManyField(User)
    image = ImageField('Image name', upload_to='projects_images', null=True)

    def __str__(self):
        return "{}".format(self.name)


class File(Model):
    """ Модель хранения пути к файлу """

    project_name = ForeignKey(Project, verbose_name='Project name',
                              on_delete=CASCADE, null=True)
    name = CharField('File name', max_length=200)
    path = FileField(max_length=200, upload_to='zip_files')

    def __str__(self):
        return "{}".format(self.name)


class News(Model):
    """ Модель хранения новости """

    user = ForeignKey(User, verbose_name='User', on_delete=CASCADE)
    headline = CharField('Headline', max_length=150)
    text = TextField('Text', max_length=600)
    pub_date = DateTimeField('Date published', auto_now_add=True)
    zip_file = ManyToManyField(File)
    image = ImageField('Image name', upload_to='images')

    def __str__(self):
        return "{} - {}".format(self.id, self.headline)


class Comment(Model):
    """ Модель хранения комментария """

    news_id = PositiveIntegerField(null=True)
    user = ForeignKey(User, on_delete=CASCADE)
    text = TextField(max_length=300)
    like = IntegerField(default=0)
    to_show = BooleanField(default=True)

    def __str__(self):
        return "{} - {}".format(self.user, self.news_id)

from django.db.models import (ImageField, DateTimeField,
                              TextField, FileField,
                              CharField, ForeignKey,
                              Model, CASCADE)


class User(Model):
    """ Модель для пользователей"""

    nick_name = CharField(max_length=50)
    email = CharField(max_length=126)
    password = TextField(max_length=254)


class Main(Model):
    """ Модель хранения новости """

    user = ForeignKey(User, verbose_name="User", on_delete=CASCADE)
    headline = CharField('Headline', max_length=150)
    text = TextField('Text', max_length=500)
    pub_date = DateTimeField('date published', auto_now_add=True)
    main_image = ImageField('Image_name')

    def __str__(self):
        return "{}".format(self.user)


class Files(Model):
    """ Модель хранения пути к файлу """

    news = ForeignKey(Main, on_delete=CASCADE)
    file_name = CharField('File name', max_length=200)
    file_path = FileField(max_length=200)

from django.db.models import (ImageField, DateTimeField,
                              TextField, FileField,
                              CharField, ForeignKey,
                              Model, CASCADE,
                              ManyToManyField)


class User(Model):
    """ Модель для пользователя """

    nick_name = CharField(max_length=50)
    email = CharField(max_length=120)
    password = CharField(max_length=60)

    def __str__(self):
        return "{}".format(self.nick_name)


class Project(Model):
    """ Модель хранения информации о проекте"""

    project_name = CharField(max_length=100)
    description_of_project = TextField(max_length=1000, null=True)
    staff_name = ManyToManyField(User)

    def __str__(self):
        return "{}".format(self.project_name)


class File(Model):
    """ Модель хранения пути к файлу """

    project_name = ForeignKey(Project, verbose_name='Project name',
                              on_delete=CASCADE, null=True)
    file_name = CharField('File name', max_length=200)
    file_path = FileField(max_length=200, upload_to='zip_files')

    def __str__(self):
        return "{}".format(self.file_name)


class News(Model):
    """ Модель хранения новости """

    user = ForeignKey(User, verbose_name='User', on_delete=CASCADE)
    headline = CharField('Headline', max_length=150)
    text = TextField('Text', max_length=600)
    pub_date = DateTimeField('Date published', auto_now_add=True)
    zip_file = ManyToManyField(File)
    main_image = ImageField('Image name', upload_to='images')

    def __str__(self):
        return "{}".format(self.user)

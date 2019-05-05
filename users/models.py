from django.contrib.auth.models import User
from django.db.models import (ImageField, Model, OneToOneField,
                              BooleanField, CharField, CASCADE)


class Profile(Model):
    """ Модель для пользователя """

    user = OneToOneField(User, on_delete=CASCADE, primary_key=True)
    name = CharField(max_length=50)
    to_show = BooleanField(default=False)
    staff_position = CharField(max_length=100, default="")
    image = ImageField('Avatar', upload_to='user_images', null=True)

    def __str__(self):
        return "{}".format(self.name)

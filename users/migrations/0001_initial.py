# Generated by Django 2.1.7 on 2019-05-05 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=50)),
                ('to_show', models.BooleanField(default=False)),
                ('staff_position', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(null=True, upload_to='user_images', verbose_name='Avatar')),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-17 15:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(default='', max_length=20, validators=[django.core.validators.RegexValidator(message='invalid format number. Example: 0859325039 ', regex='(03|05|07|08|09|01[2|6|8|9])+([0-9]{8})')]),
        ),
    ]
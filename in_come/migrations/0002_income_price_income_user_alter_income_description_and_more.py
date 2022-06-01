# Generated by Django 4.0.4 on 2022-05-17 15:08

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('in_come', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=18, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AddField(
            model_name='income',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='income',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='income',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]

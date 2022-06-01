# Generated by Django 4.0.4 on 2022-04-21 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('updatedAt', models.DateTimeField(auto_now=True, null=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('name', models.CharField(choices=[('NEC', 'Nec'), ('FFA', 'Ffa'), ('LTSS', 'Ltss'), ('EDU', 'Edu'), ('PLAY', 'Play'), ('GIVEN', 'Given')], default='', max_length=10)),
                ('percent', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jars', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

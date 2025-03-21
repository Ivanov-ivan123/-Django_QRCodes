# Generated by Django 5.1.5 on 2025-02-17 11:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_qr', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('expire_date', models.DateTimeField(null=True)),
                ('costomization', models.CharField(max_length=255, null=True)),
                ('url', models.URLField()),
                ('color', models.CharField(max_length=40)),
                ('bgcolour', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('center_image', models.ImageField(null=True, upload_to='')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

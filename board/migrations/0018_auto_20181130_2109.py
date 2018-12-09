# Generated by Django 2.1.3 on 2018-11-30 12:09

import board.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0017_auto_20181130_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freeimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='free/%Y/%m/%d/orig', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='freepost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=board.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='noticeimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='notice%Y/%m/%d/orig', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='proposalimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='proposal/%Y/%m/%d/orig', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='reportimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='report/%Y/%m/%d/orig', verbose_name='Image'),
        ),
    ]

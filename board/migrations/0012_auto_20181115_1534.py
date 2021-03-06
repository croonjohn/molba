# Generated by Django 2.1.3 on 2018-11-15 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0011_auto_20181115_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freecomment',
            name='published_datetime',
        ),
        migrations.RemoveField(
            model_name='freepost',
            name='published_datetime',
        ),
        migrations.RemoveField(
            model_name='noticecomment',
            name='published_datetime',
        ),
        migrations.RemoveField(
            model_name='noticepost',
            name='published_datetime',
        ),
        migrations.RemoveField(
            model_name='proposalcomment',
            name='published_datetime',
        ),
        migrations.RemoveField(
            model_name='proposalpost',
            name='published_datetime',
        ),
        migrations.RemoveField(
            model_name='reportcomment',
            name='published_datetime',
        ),
        migrations.RemoveField(
            model_name='reportpost',
            name='published_datetime',
        ),
        migrations.AddField(
            model_name='freecomment',
            name='published_date_only',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='freepost',
            name='published_date_only',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='noticecomment',
            name='published_date_only',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='noticepost',
            name='published_date_only',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='proposalcomment',
            name='published_date_only',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='proposalpost',
            name='published_date_only',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='reportcomment',
            name='published_date_only',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='reportpost',
            name='published_date_only',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='freecomment',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='freepost',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='noticecomment',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='noticepost',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='proposalcomment',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='proposalpost',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='reportcomment',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='reportpost',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

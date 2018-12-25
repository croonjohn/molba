# Generated by Django 2.1.3 on 2018-11-28 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0015_auto_20181125_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d/orig', verbose_name='Image')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='board.FreePost')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NoticeImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d/orig', verbose_name='Image')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='board.NoticePost')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProposalImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d/orig', verbose_name='Image')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='board.ProposalPost')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReportImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d/orig', verbose_name='Image')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='board.ReportPost')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
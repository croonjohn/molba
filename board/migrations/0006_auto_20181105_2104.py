# Generated by Django 2.1.3 on 2018-11-05 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_freecomment_noticecomment_proposalcomment_reportcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freecomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='freecomments', to='board.FreePost'),
        ),
        migrations.AlterField(
            model_name='noticecomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noticecomments', to='board.NoticePost'),
        ),
        migrations.AlterField(
            model_name='proposalcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposalcomments', to='board.ProposalPost'),
        ),
        migrations.AlterField(
            model_name='reportcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reportcomments', to='board.ReportPost'),
        ),
    ]

# Generated by Django 3.2.5 on 2023-01-10 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0009_auto_20230110_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetbasic',
            name='memo',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='備註'),
        ),
        migrations.AlterField(
            model_name='assetmove',
            name='memo',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='備註'),
        ),
        migrations.AlterField(
            model_name='syuser',
            name='username',
            field=models.CharField(max_length=16, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='userarea',
            name='memo',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='備註'),
        ),
        migrations.AlterField(
            model_name='userunit',
            name='memo',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='備註'),
        ),
    ]

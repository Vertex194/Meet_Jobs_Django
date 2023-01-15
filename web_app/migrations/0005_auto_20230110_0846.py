# Generated by Django 3.2.5 on 2023-01-10 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0004_auto_20230110_0840'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assetbasic',
            options={'verbose_name': '資產基本檔', 'verbose_name_plural': '資產基本檔'},
        ),
        migrations.AlterModelOptions(
            name='assetmove',
            options={'verbose_name': '資產移轉單', 'verbose_name_plural': '資產移轉單'},
        ),
        migrations.AlterModelOptions(
            name='syuser',
            options={'verbose_name': '員工基本檔', 'verbose_name_plural': '員工基本檔'},
        ),
        migrations.AlterModelOptions(
            name='userarea',
            options={'verbose_name': '所屬區域資料檔', 'verbose_name_plural': '所屬區域資料檔'},
        ),
        migrations.AlterModelOptions(
            name='userunit',
            options={'verbose_name': '所屬單位資料檔', 'verbose_name_plural': '所屬單位資料檔'},
        ),
        migrations.AlterModelTable(
            name='assetbasic',
            table=None,
        ),
        migrations.AlterModelTable(
            name='assetmove',
            table=None,
        ),
        migrations.AlterModelTable(
            name='userarea',
            table=None,
        ),
        migrations.AlterModelTable(
            name='userunit',
            table=None,
        ),
    ]

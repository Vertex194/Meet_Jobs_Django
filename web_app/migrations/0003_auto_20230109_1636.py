# Generated by Django 3.2.5 on 2023-01-09 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_auto_20230109_1511'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='assetbasic',
            table='資產基本檔',
        ),
        migrations.AlterModelTable(
            name='assetmove',
            table='資產移轉記錄檔',
        ),
        migrations.AlterModelTable(
            name='syuser',
            table='員工基本檔',
        ),
        migrations.AlterModelTable(
            name='userarea',
            table='所屬區域資料檔',
        ),
        migrations.AlterModelTable(
            name='userunit',
            table='所屬單位資料檔',
        ),
    ]

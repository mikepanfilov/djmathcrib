# Generated by Django 3.1 on 2020-08-24 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200821_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='inviteduser',
            name='invite_key',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Инвайт ключ'),
        ),
    ]

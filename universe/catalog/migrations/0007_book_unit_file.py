# Generated by Django 4.0.5 on 2022-06-21 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_author_biography'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='unit_file',
            field=models.FileField(blank=True, help_text='Загрузите электронный вариант', null=True, upload_to='', verbose_name='Электронный экземпляр'),
        ),
    ]

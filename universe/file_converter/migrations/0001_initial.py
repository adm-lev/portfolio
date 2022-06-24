# Generated by Django 4.0.5 on 2022-06-24 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OperationFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_file', models.FileField(blank=True, help_text='Загрузите документ', null=True, upload_to='converter/files', verbose_name='Документ')),
                ('picture', models.ImageField(blank=True, help_text='Загрузите картинку', null=True, upload_to='converter/images', verbose_name='Изображение')),
            ],
        ),
    ]
# Generated by Django 2.0.1 on 2018-02-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_adresurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjektUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(default='domain.com', max_length=2000, verbose_name='Projekt Url')),
            ],
        ),
        migrations.DeleteModel(
            name='AdresUrl',
        ),
    ]

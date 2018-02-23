# Generated by Django 2.0.2 on 2018-02-21 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180221_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshortner',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='urlshortner',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='urlshortner',
            name='shortcode',
            field=models.CharField(blank=True, max_length=16, unique=True),
        ),
    ]

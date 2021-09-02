# Generated by Django 3.1 on 2020-10-27 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20201017_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='talent',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='talent',
            name='bio',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]

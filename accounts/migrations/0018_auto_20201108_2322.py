# Generated by Django 3.1 on 2020-11-09 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_remove_talent_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='talent',
            name='current_employment',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='talent',
            name='degree_education',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='talent',
            name='institution_education',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='talent',
            name='position_employment',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='talent',
            name='yearend_education',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='talent',
            name='yearend_employment',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='talent',
            name='yearstart_education',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='talent',
            name='yearstart_employment',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

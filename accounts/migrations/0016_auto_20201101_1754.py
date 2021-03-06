# Generated by Django 3.1 on 2020-11-01 22:54

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('accounts', '0015_talent_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='talent',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='talent',
            name='emailprofile',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='talent',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

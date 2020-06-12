# Generated by Django 3.0.7 on 2020-06-12 15:50

import autoslug.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cheeses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheese',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='cheese',
            name='firmness',
            field=models.CharField(choices=[('unspecified', 'Unspecified'), ('soft', 'Soft'), ('semi-soft', 'Semi-Soft'), ('semi-hard', 'Semi-Hard'), ('hard', 'Hard')], default='unspecified', max_length=20, verbose_name='Firmness'),
        ),
        migrations.AddField(
            model_name='cheese',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=django.utils.timezone.now, editable=False, populate_from='name', unique=True, verbose_name='Cheese Address'),
            preserve_default=False,
        ),
    ]

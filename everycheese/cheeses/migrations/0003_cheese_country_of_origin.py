# Generated by Django 3.0.7 on 2020-06-13 09:45

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cheeses', '0002_auto_20200612_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheese',
            name='country_of_origin',
            field=django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='Country of Origin'),
        ),
    ]
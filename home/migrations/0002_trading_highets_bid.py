# Generated by Django 3.0.7 on 2020-08-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trading',
            name='highets_bid',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.0.7 on 2020-08-19 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0014_bidding_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trading',
            name='seller',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trading_seller', to=settings.AUTH_USER_MODEL),
        ),
    ]

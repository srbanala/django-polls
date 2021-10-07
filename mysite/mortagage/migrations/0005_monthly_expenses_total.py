# Generated by Django 2.0.7 on 2020-08-22 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortagage', '0004_monthly_expenses'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthly_expenses',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]

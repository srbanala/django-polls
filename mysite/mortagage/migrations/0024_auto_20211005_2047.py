# Generated by Django 2.0.7 on 2021-10-05 20:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortagage', '0023_auto_20211005_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthly_expenses',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 5, 20, 47, 25, 714210)),
        ),
    ]

# Generated by Django 2.0.7 on 2021-10-05 22:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortagage', '0025_auto_20211005_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthly_expenses',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 5, 22, 0, 43, 270213)),
        ),
    ]

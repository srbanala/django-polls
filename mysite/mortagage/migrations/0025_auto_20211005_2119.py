# Generated by Django 2.0.7 on 2021-10-05 21:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortagage', '0024_auto_20211005_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthly_expenses',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 5, 21, 19, 22, 997675)),
        ),
    ]

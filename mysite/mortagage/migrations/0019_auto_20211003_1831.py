# Generated by Django 2.0.7 on 2021-10-03 22:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mortagage', '0018_auto_20211003_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='fabonacci_number',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='file_upload',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='image_upload',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='media_store',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='monthly_expenses',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='monthly_expenses',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 3, 22, 31, 41, 356821, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='monthly_payment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='remaining_balance',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user_login',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

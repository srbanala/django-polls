# Generated by Django 2.0.7 on 2020-08-19 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortagage', '0003_delete_monthly_expenses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monthly_Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')),
                ('item', models.CharField(max_length=20)),
                ('price', models.FloatField()),
            ],
        ),
    ]

# Generated by Django 2.0.7 on 2020-08-19 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortgage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monthly_Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=20)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Remaining_Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal', models.IntegerField()),
                ('interest', models.FloatField()),
                ('duration', models.IntegerField()),
                ('no_of_payments_made', models.IntegerField(default=0)),
                ('amount_due', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='monthly_payment',
            name='payment',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='monthly_payment',
            name='interest',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
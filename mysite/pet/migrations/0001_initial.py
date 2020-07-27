# Generated by Django 3.0.8 on 2020-07-27 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('folio', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('redemption_date', models.DateField()),
            ],
        ),
    ]

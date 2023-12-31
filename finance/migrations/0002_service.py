# Generated by Django 4.2.2 on 2023-12-26 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_phone', models.CharField(max_length=15)),
                ('client_email', models.EmailField(max_length=254)),
                ('service_description', models.CharField(max_length=255)),
                ('months_valid', models.IntegerField()),
                ('due_date', models.DateField()),
                ('amount_due', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]

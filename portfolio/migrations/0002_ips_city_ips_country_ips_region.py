# Generated by Django 4.1.5 on 2023-02-04 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ips',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='ips',
            name='country',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='ips',
            name='region',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
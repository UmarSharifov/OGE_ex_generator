# Generated by Django 3.2 on 2021-05-09 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OGE', '0003_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='Lvl',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
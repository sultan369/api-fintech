# Generated by Django 2.2.1 on 2019-05-14 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('made', 'made'), ('missed', 'missed')], db_column='type', max_length=6, verbose_name='status'),
        ),
    ]
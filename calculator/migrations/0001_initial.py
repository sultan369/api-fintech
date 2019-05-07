# Generated by Django 2.2.1 on 2019-05-07 01:58

from decimal import Decimal
import django.contrib.postgres.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.contrib.postgres.validators.RangeMinValueValidator(Decimal('0.01'))], verbose_name='Amount')),
                ('term', models.IntegerField(validators=[django.contrib.postgres.validators.RangeMinValueValidator(1)], verbose_name='Term')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.contrib.postgres.validators.RangeMinValueValidator(Decimal('0.01'))], verbose_name='Rate')),
                ('date_initial', models.DateTimeField(verbose_name='Date creation')),
            ],
            options={
                'verbose_name': 'Loan',
                'verbose_name_plural': 'Loans',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('MD', 'Made'), ('MS', 'Missed')], default='MD', max_length=2, verbose_name='Type')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.contrib.postgres.validators.RangeMinValueValidator(Decimal('0.01'))], verbose_name='Amount')),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.Loan')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]
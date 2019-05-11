# Generated by Django 2.2.1 on 2019-05-11 02:51

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('surname', models.CharField(max_length=30, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.BigIntegerField(verbose_name='Phone')),
                ('cpf', models.BigIntegerField(unique=True, verbose_name='CPF')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Amount')),
                ('term', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Term')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Rate')),
                ('date_initial', models.DateTimeField(verbose_name='Date creation')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='calculator.Client')),
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
                ('status', models.CharField(choices=[('made', 'made'), ('missed', 'missed')], db_column='type', max_length=2, verbose_name='status')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Amount')),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.Loan')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]

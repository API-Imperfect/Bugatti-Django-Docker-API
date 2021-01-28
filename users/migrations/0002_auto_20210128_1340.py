# Generated by Django 3.1.5 on 2021-01-28 13:40

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=django_countries.fields.CountryField(default='KE', max_length=2, verbose_name='Your country'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6, verbose_name='Your Gender'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='net_worth',
            field=models.CharField(default='0 dollars', max_length=255, verbose_name='Your estimated net worth'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default='1234', max_length=40, verbose_name='Your Phone number'),
            preserve_default=False,
        ),
    ]
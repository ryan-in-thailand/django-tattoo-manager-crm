# Generated by Django 3.1.12 on 2021-06-17 10:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=30)),
                ('commission', models.PositiveSmallIntegerField(help_text='Enter a number from 0-100', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Commission %')),
                ('is_manager', models.BooleanField(help_text='Check this box to give manager permissions.', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(default='Guest', max_length=30)),
                ('customer_email', models.EmailField(blank=True, max_length=50, null=True)),
                ('customer_facebook_name', models.CharField(blank=True, max_length=30, null=True)),
                ('customer_instagram', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TattooShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField()),
                ('tattoo_description', models.TextField(max_length=300)),
                ('custom_design', models.BooleanField(help_text='Check the box if the         customer needs a custom design', null=True)),
                ('custom_design_finished', models.BooleanField(help_text='Check the box         if the design is finalized', null=True)),
                ('deposit_amount', models.DecimalField(blank=True, decimal_places=2, help_text='Enter only if a customer paid a deposit', max_digits=7, null=True)),
                ('deposit_date', models.DateField(blank=True, null=True)),
                ('quote', models.CharField(blank=True, help_text='If you gave a quoted price, enter it here to remember', max_length=30)),
                ('final_payment', models.DecimalField(decimal_places=2, max_digits=5)),
                ('artist_paid', models.BooleanField(default=False, help_text="Check here after you've paid your artist")),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tattoo_shop.artist')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tattoo_shop.customer')),
                ('tattoo_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tattoo_shop.tattooshop')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='tattoo_shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tattoo_shop.tattooshop'),
        ),
        migrations.AddField(
            model_name='artist',
            name='tattoo_shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tattoo_shop.tattooshop'),
        ),
    ]

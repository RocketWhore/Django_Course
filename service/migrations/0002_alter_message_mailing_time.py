# Generated by Django 4.2.4 on 2023-08-26 16:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='mailing_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='время рассылки'),
        ),
    ]
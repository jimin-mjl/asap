# Generated by Django 3.2.3 on 2021-05-31 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210531_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='postal_code',
            field=models.CharField(blank=True, max_length=50, verbose_name='Postal Code'),
        ),
    ]
# Generated by Django 2.2.5 on 2019-11-06 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opora', '0005_auto_20191104_1414'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='politicalparty',
            options={'verbose_name_plural': 'political parties'},
        ),
        migrations.AlterModelOptions(
            name='transactionpages',
            options={'verbose_name_plural': 'transaction pages'},
        ),
        migrations.AlterUniqueTogether(
            name='transactionpages',
            unique_together=set(),
        ),
    ]

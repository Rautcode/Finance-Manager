# Generated by Django 4.1.7 on 2023-03-08 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_delete_monthlytransaction_alter_transaction_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]

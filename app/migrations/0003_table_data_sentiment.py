# Generated by Django 3.2.8 on 2021-10-09 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_table_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='table_data',
            name='sentiment',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

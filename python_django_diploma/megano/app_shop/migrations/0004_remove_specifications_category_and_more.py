# Generated by Django 4.1 on 2023-02-06 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0003_alter_manufacturer_options_alter_manufacturer_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specifications',
            name='category',
        ),
        migrations.DeleteModel(
            name='GoodSpecification',
        ),
        migrations.DeleteModel(
            name='Specifications',
        ),
    ]
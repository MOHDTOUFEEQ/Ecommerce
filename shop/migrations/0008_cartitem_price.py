# Generated by Django 4.2.4 on 2023-12-17 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_cartitem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
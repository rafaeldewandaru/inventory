# Generated by Django 4.2.5 on 2023-10-09 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_product_album'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='album_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='album',
            new_name='link',
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-27 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_kategori_nama_kategori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='nama_status',
            field=models.CharField(),
        ),
    ]

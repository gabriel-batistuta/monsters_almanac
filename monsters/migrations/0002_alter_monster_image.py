# Generated by Django 5.0 on 2023-12-27 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='monsters/'),
        ),
    ]

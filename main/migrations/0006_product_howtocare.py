# Generated by Django 4.0.3 on 2022-05-21 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_petinstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='howtocare',
            field=models.CharField(db_index=True, default='Это монстр, уход не нужен, он тебе поможет', max_length=300),
        ),
    ]
# Generated by Django 4.0.3 on 2022-04-30 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CRUD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('comment', models.TextField(default='Здесь крч хорошая птица и неплохой бэкенд')),
            ],
        ),
    ]
# Generated by Django 4.1.5 on 2023-01-20 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('marks', models.CharField(max_length=20)),
            ],
        ),
    ]

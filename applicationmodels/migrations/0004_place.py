# Generated by Django 2.2 on 2019-04-10 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicationmodels', '0003_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, verbose_name='Назва')),
                ('address', models.TextField(max_length=50, verbose_name='Адреса')),
            ],
        ),
    ]

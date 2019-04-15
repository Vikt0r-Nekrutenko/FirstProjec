# Generated by Django 2.2 on 2019-04-10 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicationmodels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, verbose_name="Iм'я")),
                ('surname', models.TextField(max_length=50, verbose_name='Прiзвище')),
                ('birthday', models.DateField(verbose_name='День народження')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Автори',
            },
        ),
    ]
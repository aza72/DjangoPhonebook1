# Generated by Django 5.0.1 on 2024-01-12 05:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Наименование организации')),
            ],
            options={
                'verbose_name': 'Организации',
                'verbose_name_plural': 'Организации',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='имя')),
                ('surname', models.CharField(max_length=50, verbose_name='фамилия')),
                ('second_name', models.CharField(max_length=20, verbose_name='отчество')),
                ('position', models.CharField(max_length=150, verbose_name='должность')),
                ('phone', models.CharField(max_length=20, verbose_name='телефон')),
                ('short_phone', models.CharField(max_length=20, verbose_name='короткий №')),
                ('cabinet', models.CharField(max_length=20, verbose_name='кабинет')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='дата и время обновления')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='phonebook.division', verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Телефонны',
                'verbose_name_plural': 'Телефонны',
                'ordering': ['-create_at'],
            },
        ),
    ]

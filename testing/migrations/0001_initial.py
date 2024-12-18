# Generated by Django 5.1.4 on 2024-12-12 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crossref',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('authors', models.CharField(max_length=256)),
                ('doi', models.CharField(max_length=32)),
                ('updated', models.DateTimeField()),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-02 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tittle', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

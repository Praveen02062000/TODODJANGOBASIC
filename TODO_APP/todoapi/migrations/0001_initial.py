# Generated by Django 5.1.4 on 2024-12-11 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TODOTABLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todovalue', models.CharField(max_length=1000)),
                ('todostatus', models.BooleanField()),
            ],
        ),
    ]
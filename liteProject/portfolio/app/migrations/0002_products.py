# Generated by Django 4.1.5 on 2023-01-26 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='')),
                ('p_name', models.CharField(max_length=50)),
                ('p_id', models.CharField(max_length=50)),
                ('p_price', models.IntegerField(max_length=50)),
            ],
        ),
    ]
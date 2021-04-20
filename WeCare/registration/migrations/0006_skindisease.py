# Generated by Django 3.0.2 on 2021-02-27 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20210227_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkinDisease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, unique=True)),
                ('image1', models.ImageField(upload_to='images/')),
                ('image2', models.ImageField(upload_to='images/')),
                ('image3', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
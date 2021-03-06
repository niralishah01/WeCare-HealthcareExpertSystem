# Generated by Django 3.0.2 on 2021-03-19 21:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0016_auto_20210320_0255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que_text', models.CharField(max_length=2000, unique=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans_text', models.CharField(max_length=3000)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('que_text', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='registration.Questions')),
            ],
        ),
    ]

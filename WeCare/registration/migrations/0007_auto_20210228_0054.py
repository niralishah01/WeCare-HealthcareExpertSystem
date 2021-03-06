# Generated by Django 3.0.2 on 2021-02-27 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_skindisease'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='associate_hospital',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Hospital'),
        ),
        migrations.CreateModel(
            name='DiseaseTreatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('duratioin', models.CharField(max_length=100)),
                ('Disease_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Disease')),
            ],
        ),
    ]

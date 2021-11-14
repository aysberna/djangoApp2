# Generated by Django 3.2.9 on 2021-11-13 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('collection_frequency', models.IntegerField()),
                ('last_collection', models.DateTimeField()),
                ('operation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evreka2.operation')),
            ],
        ),
    ]

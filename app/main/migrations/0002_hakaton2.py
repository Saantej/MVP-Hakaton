# Generated by Django 4.2.6 on 2023-10-26 04:33

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0001_initial'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hakaton2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview', models.FileField(upload_to=main.models.get_file_path, verbose_name='Фотография')),
                ('description', models.TextField(max_length=300)),
                ('prize_fund', models.BigIntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regions.city')),
            ],
        ),
    ]
# Generated by Django 5.1 on 2024-09-09 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='Unknown', max_length=50)),
                ('Phone', models.CharField(default=1, max_length=11)),
                ('Adress', models.CharField(default='Unknown', max_length=100)),
                ('Specialization', models.CharField(default='Unknown', max_length=50)),
            ],
        ),
    ]

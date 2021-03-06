# Generated by Django 3.2.5 on 2021-09-20 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='deportment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deportment_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='empoloy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=30)),
                ('e_email', models.EmailField(max_length=254)),
                ('e_sal', models.FloatField()),
                ('address', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('emp_id', models.ManyToManyField(to='venkat_app.deportment')),
            ],
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-31 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RouterInfo',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('sapid', models.CharField(max_length=18)),
                ('hostname', models.CharField(max_length=14)),
                ('loopback', models.GenericIPAddressField(protocol='IPv4')),
                ('mac_address', models.CharField(max_length=17)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'router_info',
            },
        ),
    ]

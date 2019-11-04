# Generated by Django 2.2.6 on 2019-10-31 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0002_auto_20191031_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reparation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_installaion', models.DateTimeField(blank=True, null=True)),
                ('frais', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descriptif', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
            ],
        ),
    ]

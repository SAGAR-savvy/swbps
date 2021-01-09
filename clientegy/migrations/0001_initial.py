# Generated by Django 3.1.4 on 2020-12-13 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('age', models.PositiveIntegerField()),
                ('phone_no', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('dev_id', models.AutoField(primary_key=True, serialize=False)),
                ('age', models.PositiveIntegerField()),
                ('exp', models.TextField()),
                ('charging_basis', models.TextField()),
                ('domain', models.TextField()),
                ('phone_no', models.CharField(max_length=10)),
                ('sample_project_url', models.URLField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('domain', models.TextField()),
                ('lvl_exp', models.TextField()),
                ('Offered_price', models.IntegerField()),
                ('proj_selected_flag', models.BooleanField(default=False)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientegy.client')),
            ],
        ),
        migrations.CreateModel(
            name='PSRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_price', models.PositiveIntegerField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientegy.client')),
                ('dev_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientegy.developer')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientegy.project')),
            ],
        ),
        migrations.CreateModel(
            name='Final_bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=None)),
                ('bid_price', models.PositiveIntegerField()),
                ('project_finished', models.BooleanField(default=False)),
                ('review', models.TextField(blank=True)),
                ('feedback', models.TextField(blank=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clientegy.client')),
                ('dev_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clientegy.developer')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clientegy.project')),
            ],
        ),
    ]

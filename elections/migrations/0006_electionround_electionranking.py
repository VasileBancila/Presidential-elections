# Generated by Django 5.0 on 2024-03-29 20:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0005_remove_profile_is_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectionRound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('finalized', models.BooleanField(default=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ElectionRanking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(max_length=100)),
                ('rank', models.PositiveIntegerField()),
                ('election_round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.electionround')),
            ],
        ),
    ]

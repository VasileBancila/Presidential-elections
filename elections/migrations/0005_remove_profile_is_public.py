# Generated by Django 5.0 on 2024-03-23 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0004_remove_candidate_user_profile_election_candidacy_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_public',
        ),
    ]

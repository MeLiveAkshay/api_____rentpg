# Generated by Django 5.2 on 2025-06-21 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('member_name', models.CharField(max_length=100)),
                ('member_role', models.CharField(max_length=100)),
                ('member_bio', models.TextField()),
                ('github_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
                ('member_image', models.URLField(blank=True, null=True)),
            ],
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-19 22:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("authentik_policies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="IPReputation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ip", models.GenericIPAddressField(unique=True)),
                ("score", models.IntegerField(default=0)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="ReputationPolicy",
            fields=[
                (
                    "policy_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="authentik_policies.Policy",
                    ),
                ),
                ("check_ip", models.BooleanField(default=True)),
                ("check_username", models.BooleanField(default=True)),
                ("threshold", models.IntegerField(default=-5)),
            ],
            options={
                "verbose_name": "Reputation Policy",
                "verbose_name_plural": "Reputation Policies",
            },
            bases=("authentik_policies.policy",),
        ),
        migrations.CreateModel(
            name="UserReputation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("score", models.IntegerField(default=0)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
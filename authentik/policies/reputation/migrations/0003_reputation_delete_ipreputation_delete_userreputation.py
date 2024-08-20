# Generated by Django 4.0.1 on 2022-01-05 18:56

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_policies_reputation", "0002_auto_20210529_2046"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reputation",
            fields=[
                (
                    "reputation_uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("identifier", models.TextField()),
                ("ip", models.GenericIPAddressField()),
                ("ip_geo_data", models.JSONField(default=dict)),
                ("score", models.BigIntegerField(default=0)),
                ("updated", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "unique_together": {("identifier", "ip")},
            },
        ),
        migrations.DeleteModel(
            name="IPReputation",
        ),
        migrations.DeleteModel(
            name="UserReputation",
        ),
    ]
# Generated by Django 3.1.1 on 2020-09-16 21:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_providers_oauth2", "0002_oauth2provider_sub_mode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="oauth2provider",
            name="client_type",
            field=models.CharField(
                choices=[("confidential", "Confidential"), ("public", "Public")],
                default="confidential",
                help_text=(
                    "Confidential clients are capable of maintaining the confidentiality\n    of"
                    " their credentials. Public clients are incapable."
                ),
                max_length=30,
                verbose_name="Client Type",
            ),
        ),
        migrations.AlterField(
            model_name="oauth2provider",
            name="response_type",
            field=models.TextField(
                choices=[
                    ("code", "code (Authorization Code Flow)"),
                    ("id_token", "id_token (Implicit Flow)"),
                    ("id_token token", "id_token token (Implicit Flow)"),
                    ("code token", "code token (Hybrid Flow)"),
                    ("code id_token", "code id_token (Hybrid Flow)"),
                    ("code id_token token", "code id_token token (Hybrid Flow)"),
                ],
                default="code",
                help_text="Response Type required by the client.",
            ),
        ),
    ]
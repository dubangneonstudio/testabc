# Generated by Django 4.0.4 on 2022-04-14 20:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "authentik_stages_authenticator_webauthn",
            "0006_authenticatewebauthnstage_authenticator_attachment_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="webauthndevice",
            old_name="last_used_on",
            new_name="last_t",
        ),
    ]

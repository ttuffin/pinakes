# Generated by Django 4.0.2 on 2022-03-23 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0036_portfolio_share_count"),
    ]

    operations = [
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the notification method",
                        max_length=128,
                    ),
                ),
                (
                    "setting_schema",
                    models.JSONField(
                        blank=True,
                        help_text="JSON schema of the notification method",
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="notification",
            constraint=models.CheckConstraint(
                check=models.Q(("name__length__gt", 0)),
                name="main_notification_name_empty",
            ),
        ),
        migrations.AddConstraint(
            model_name="notification",
            constraint=models.UniqueConstraint(
                fields=("name",), name="main_notification_name_unique"
            ),
        ),
        migrations.AddField(
            model_name="template",
            name="process_method",
            field=models.ForeignKey(
                help_text=(
                    "ID of the notification method for processing the workflow"
                ),
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="process_notification",
                to="main.notification",
            ),
        ),
        migrations.AddField(
            model_name="template",
            name="signal_method",
            field=models.ForeignKey(
                help_text=(
                    "ID of the notification method for signaling the "
                    "completion of the workflow",
                ),
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="signal_notification",
                to="main.notification",
            ),
        ),
    ]

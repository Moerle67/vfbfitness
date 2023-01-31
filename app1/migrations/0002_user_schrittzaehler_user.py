# Generated by Django 4.1.5 on 2023-01-31 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=50)),
                ("vorname", models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name="schrittzaehler",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="app1.user",
                verbose_name="Benutzer ",
            ),
            preserve_default=False,
        ),
    ]
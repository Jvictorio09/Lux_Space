# Generated manually for Service cta_heading and cta_intro

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0004_rename_is_featured_to_featured"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="cta_heading",
            field=models.CharField(
                blank=True,
                help_text="Bottom CTA section heading, e.g. 'Ready to Transform Your Landscape?'.",
                max_length=200,
            ),
        ),
        migrations.AddField(
            model_name="service",
            name="cta_intro",
            field=models.TextField(
                blank=True,
                help_text="Bottom CTA paragraph under heading.",
            ),
        ),
    ]

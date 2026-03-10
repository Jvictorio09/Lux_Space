# Project detail page dynamic content

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0005_service_cta_heading_cta_intro"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="pull_quote",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="pull_quote_author",
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name="project",
            name="testimonial_quote",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="testimonial_author",
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name="project",
            name="testimonial_location",
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.AddField(
            model_name="project",
            name="testimonial_avatar_url",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="challenges",
            field=models.JSONField(
                blank=True,
                default=list,
                help_text="List of {title, description}.",
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="solutions",
            field=models.JSONField(
                blank=True,
                default=list,
                help_text="List of {title, description}. Should match challenges length.",
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="process_phases",
            field=models.JSONField(
                blank=True,
                default=list,
                help_text="List of {phase_label, duration, title, description, icon, is_last}.",
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="outcome_intro",
            field=models.TextField(
                blank=True,
                help_text="Paragraph above outcome stats.",
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="outcome_stats",
            field=models.JSONField(
                blank=True,
                default=list,
                help_text="List of {value, label}.",
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="awards",
            field=models.JSONField(
                blank=True,
                default=list,
                help_text="List of {name, title, organization, icon}.",
            ),
        ),
    ]

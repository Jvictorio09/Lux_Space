# Generated manually for Cloudinary pattern update

from django.db import migrations, models


def populate_secure_url_from_cloudinary_url(apps, schema_editor):
    """
    Data migration: Populate secure_url from cloudinary_url for existing records.
    Also populate web_url and thumb_url with the same value for backward compatibility.
    """
    GalleryImage = apps.get_model('myApp', 'GalleryImage')
    for img in GalleryImage.objects.all():
        if img.cloudinary_url and not img.secure_url:
            img.secure_url = img.cloudinary_url
            img.web_url = img.cloudinary_url  # Use same URL as fallback
            img.thumb_url = img.cloudinary_url  # Use same URL as fallback
            img.save()


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_galleryimage_alter_project_is_featured'),
    ]

    operations = [
        # Add new fields (nullable first for data migration)
        migrations.AddField(
            model_name='galleryimage',
            name='secure_url',
            field=models.URLField(blank=True, help_text='Original uploaded image URL (full quality, fallback)', null=True),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='web_url',
            field=models.URLField(blank=True, help_text='Optimized URL with f_auto,q_auto (use for website display)', null=True),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='thumb_url',
            field=models.URLField(blank=True, help_text='Thumbnail URL with c_fill,g_face,w_480,h_320 (use for galleries)', null=True),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='public_id',
            field=models.CharField(blank=True, help_text='Cloudinary public_id identifier', max_length=255),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='width',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='height',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='format',
            field=models.CharField(blank=True, help_text='Image format (webp, jpg, etc.)', max_length=10),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='bytes',
            field=models.PositiveIntegerField(blank=True, help_text='File size in bytes', null=True),
        ),
        
        # Make cloudinary_url nullable for backward compatibility
        migrations.AlterField(
            model_name='galleryimage',
            name='cloudinary_url',
            field=models.URLField(blank=True, help_text='Legacy field - use secure_url instead'),
        ),
        
        # Data migration: populate new fields from existing cloudinary_url
        migrations.RunPython(populate_secure_url_from_cloudinary_url, migrations.RunPython.noop),
        
        # Now make secure_url, web_url, thumb_url required (after data migration)
        migrations.AlterField(
            model_name='galleryimage',
            name='secure_url',
            field=models.URLField(help_text='Original uploaded image URL (full quality, fallback)'),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='web_url',
            field=models.URLField(help_text='Optimized URL with f_auto,q_auto (use for website display)'),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='thumb_url',
            field=models.URLField(help_text='Thumbnail URL with c_fill,g_face,w_480,h_320 (use for galleries)'),
        ),
    ]


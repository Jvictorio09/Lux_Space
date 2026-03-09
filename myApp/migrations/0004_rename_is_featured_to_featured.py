# Generated manually to fix database column name mismatch

from django.db import migrations, models


def rename_column_if_exists(apps, schema_editor):
    """Rename is_featured to featured if the column exists"""
    db_alias = schema_editor.connection.alias
    with schema_editor.connection.cursor() as cursor:
        # Check if table and column exist
        cursor.execute("""
            SELECT EXISTS (
                SELECT 1 FROM information_schema.columns 
                WHERE table_name = 'myapp_project' 
                AND column_name = 'is_featured'
            );
        """)
        exists = cursor.fetchone()[0]
        
        if exists:
            cursor.execute("ALTER TABLE myapp_project RENAME COLUMN is_featured TO featured;")


def reverse_rename(apps, schema_editor):
    """Reverse: rename featured back to is_featured"""
    db_alias = schema_editor.connection.alias
    with schema_editor.connection.cursor() as cursor:
        cursor.execute("""
            SELECT EXISTS (
                SELECT 1 FROM information_schema.columns 
                WHERE table_name = 'myapp_project' 
                AND column_name = 'featured'
            );
        """)
        exists = cursor.fetchone()[0]
        
        if exists:
            cursor.execute("ALTER TABLE myapp_project RENAME COLUMN featured TO is_featured;")


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_update_galleryimage_cloudinary_pattern'),
    ]

    operations = [
        # Rename the database column from is_featured to featured
        migrations.RunPython(rename_column_if_exists, reverse_rename),
        # Update the field definition to reflect db_column
        migrations.AlterField(
            model_name='project',
            name='is_featured',
            field=models.BooleanField(default=False, db_column='featured'),
        ),
    ]


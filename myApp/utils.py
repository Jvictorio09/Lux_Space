"""
Utility functions for image compression and Cloudinary operations.
"""
from io import BytesIO
from PIL import Image
import os


def smart_compress_to_bytes(file_obj, max_size_mb=9.3, max_width=5000):
    """
    Compress an image file to bytes, ensuring it's under max_size_mb.
    
    Logic:
    - Auto-rotate based on EXIF data
    - Convert PNG/TIFF to WebP
    - Cap dimensions at max_width (maintains aspect ratio)
    - Iteratively reduce quality until under size limit
    
    Args:
        file_obj: File-like object (Django UploadedFile or BytesIO)
        max_size_mb: Maximum file size in MB (default 9.3MB)
        max_width: Maximum width in pixels (default 5000px)
    
    Returns:
        BytesIO: Compressed image bytes
    """
    max_size_bytes = max_size_mb * 1024 * 1024  # Convert MB to bytes
    
    # Read the file
    file_obj.seek(0)
    original_bytes = file_obj.read()
    file_obj.seek(0)
    
    # If already under size limit, return original bytes
    if len(original_bytes) <= max_size_bytes:
        return BytesIO(original_bytes)
    
    # Open image with Pillow
    img = Image.open(file_obj)
    
    # Auto-rotate based on EXIF orientation
    try:
        from PIL.ExifTags import ORIENTATION
        exif = img._getexif()
        if exif is not None:
            orientation = exif.get(ORIENTATION)
            if orientation == 3:
                img = img.rotate(180, expand=True)
            elif orientation == 6:
                img = img.rotate(270, expand=True)
            elif orientation == 8:
                img = img.rotate(90, expand=True)
    except (AttributeError, KeyError, TypeError):
        # No EXIF data or can't read it
        pass
    
    # Convert to RGB if necessary (removes alpha channel, needed for WebP)
    if img.mode in ('RGBA', 'LA', 'P'):
        # Create white background for transparency
        background = Image.new('RGB', img.size, (255, 255, 255))
        if img.mode == 'P':
            img = img.convert('RGBA')
        background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
        img = background
    elif img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Resize if too wide
    if img.width > max_width:
        ratio = max_width / img.width
        new_height = int(img.height * ratio)
        img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
    
    # Try different quality levels until we're under the size limit
    quality = 90
    buffer = BytesIO()
    
    while quality >= 20:
        buffer.seek(0)
        buffer.truncate(0)
        
        # Save as WebP
        img.save(buffer, format='WEBP', quality=quality, method=6)
        
        if len(buffer.getvalue()) <= max_size_bytes:
            break
        
        quality -= 10
    
    buffer.seek(0)
    return buffer


def generate_public_id(filename):
    """
    Generate a clean public_id from filename for Cloudinary.
    
    Removes extension and sanitizes the name.
    """
    # Remove extension
    name = os.path.splitext(filename)[0]
    # Replace spaces and special chars with underscores
    import re
    name = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
    # Remove multiple underscores
    name = re.sub(r'_+', '_', name)
    # Remove leading/trailing underscores
    name = name.strip('_')
    return name.lower()


# ELA image forgery detector
from PIL import Image, ImageChops, ImageEnhance
import os

def detect_image_forgery(image_path, ela_output_path='uploads/ela_output.jpg'):
    try:
        # Convert and save a recompressed version
        original = Image.open(image_path).convert('RGB')
        temp_path = 'uploads/temp_compressed.jpg'
        original.save(temp_path, 'JPEG', quality=90)
        compressed = Image.open(temp_path)

        # ELA: compute difference
        ela_image = ImageChops.difference(original, compressed)
        extrema = ela_image.getextrema()
        max_diff = max([ex[1] for ex in extrema])

        # Boost difference to make tampering visible
        scale = 255.0 / max_diff if max_diff != 0 else 1
        ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)
        ela_image.save(ela_output_path)

        # Define threshold for suspicious forgery
        forged = max_diff > 50
        return forged, ela_output_path

    except Exception as e:
        print(f"[ELA ERROR]: {e}")
        return False, None

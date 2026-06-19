from PIL import Image
import imagehash

def calculate_hash(image_path):
    img = Image.open(image_path)
    return imagehash.phash(img)

def compare_images(image1, image2):

    hash1 = calculate_hash(image1)
    hash2 = calculate_hash(image2)

    difference = hash1 - hash2

    return {
        "hash1": str(hash1),
        "hash2": str(hash2),
        "difference": difference,
        "duplicate": difference <= 5
    }
from PIL import Image
import os
import cv2

def analyze_images(image_paths):

    results = []

    for path in image_paths:

        try:

            img = Image.open(path)

            image = cv2.imread(path)

            gray = cv2.cvtColor(
                image,
                cv2.COLOR_BGR2GRAY
            )

            blur_score = cv2.Laplacian(
                gray,
                cv2.CV_64F
            ).var()

            quality = (
                "blurry"
                if blur_score < 100
                else "good"
            )

            results.append({
                "image_id": os.path.basename(path),
                "width": img.width,
                "height": img.height,
                "blur_score": round(blur_score,2),
                "quality": quality,
                "status": "loaded"
            })

        except Exception as e:

            results.append({
                "image_id": os.path.basename(path),
                "status": "error",
                "error": str(e)
            })

    return results
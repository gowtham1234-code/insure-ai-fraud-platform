from PIL import Image
import numpy as np
import cv2


def detect_damage(image_path):

    print("PATH =", image_path)

    try:
        pil_img = Image.open(image_path).convert("RGB")
        img = np.array(pil_img)

        print("IMAGE LOADED =", img.shape)

    except Exception as e:
        print("ERROR =", e)

        return {
            "damage_detected": False,
            "damage_type": "invalid_image"
        }

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    edges = cv2.Canny(gray, 100, 200)

    edge_pixels = cv2.countNonZero(edges)

    return {
        "damage_detected": edge_pixels > 1000,
        "damage_type": "possible_damage"
    }
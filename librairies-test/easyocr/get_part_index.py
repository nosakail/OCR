import cv2
import easyocr
from PIL import Image, ImageDraw

# Télécharger le modèle
reader = easyocr.Reader(['en'], gpu=False)

# Charger l'image
im = Image.open("ant.png")

# Obtenir les boîtes englobantes
bounds = reader.readtext('ant.png')

# Dessiner les boîtes englobantes
def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.polygon([p[0] for p in [p0, p1, p2, p3]], outline=color)
    return image

# Dessiner les boîtes englobantes sur l'image
result_image = draw_boxes(im, bounds)

# Enregistrer l'image résultante
result_image.save("result.png")






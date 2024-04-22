import easyocr
import cv2

# Charger l'image
image = cv2.imread('DOTL.jpg')

# Initialiser EasyOCR avec la langue française
reader = easyocr.Reader(['fr'], gpu=False)

# Obtenir les résultats de la détection de texte
result = reader.readtext('DOTL.jpg')

# Dessiner les rectangles verts autour des zones de texte détectées
for detection in result:
    bbox = detection[0]
    cv2.rectangle(image, (bbox[0][0], bbox[0][1]), (bbox[2][0], bbox[2][1]), (0, 255, 0), 2)

# Enregistrer l'image avec les rectangles dessinés
cv2.imwrite('text_detection_output.jpg', image)

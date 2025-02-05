import cv2

# Lire l'image
image = cv2.imread('chemin/vers/votre/image.jpg')

# Vérifier si l'image a été correctement lue
if image is None:
    print("Erreur: Impossible de lire l'image.")
else:
    # Afficher l'image
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
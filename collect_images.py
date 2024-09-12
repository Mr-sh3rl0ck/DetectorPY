import cv2
import os

DATA_DIR = './data'  # Hace referencia a la carpeta 'data' en el directorio actual del script
if not os.path.exists(DATA_DIR): # Crea la carpeta 'data' si no existe
    os.makedirs(DATA_DIR)

number_of_letters = 27
dataset_size = 100

cap = cv2.VideoCapture(0) # Captura la imagen de la camara

for i in range(number_of_letters): # Itera a traves de todas las letras
    if not os.path.exists(os.path.join(DATA_DIR, str(i))): # Crea la carpeta 'i' si no existe
        os.makedirs(os.path.join(DATA_DIR, str(i)))

    print('Recolectando data para la letra {}'.format(i))
 
    done = False # variable para detener el loop
    while not done:
        ret, frame = cap.read() # Captura la imagen de la camara
        # Colocar texto en la imagen
        cv2.putText(frame, "Presiona 'q' para capturar las imagenes", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame) # Muestra la imagen capturada
        if cv2.waitKey(25) == ord('q'): # Se presiona la tecla 'q' para terminar el loop
            done = True

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read() # Captura la imagen de la camara
        cv2.imshow('frame', frame) # Muestra la imagen capturada
        cv2.waitKey(25) # Delay de 25 milisegundos
        cv2.imwrite(os.path.join(DATA_DIR, str(i), '{}.jpg'.format(counter)), frame) # Guarda la imagen capturada en la carpeta 'i'
        counter += 1

cap.release()
cv2.destroyAllWindows()

    

    
    





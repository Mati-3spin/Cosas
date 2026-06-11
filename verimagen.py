import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
dicionario = {}
imagen = mpimg.imread("imagen.jpg")
plt.imshow(imagen)
filas = imagen.shape[0]
columnas = imagen.shape[1]
canales = imagen.shape[2]
pixelarribaizq = imagen[1, 1]
pixelarribader = imagen[416, 1]
pixelabajoizq = imagen[1, 333]
pixelabajoder = imagen[416, 333]
pixelcentro = imagen[208, 167]
promedio = np.mean(imagen)
imagen = Image.open('imagen.jpg')
matriz_img = np.array(imagen)
canal_azul = matriz_img[:, :, 2]
min_azul = canal_azul.min()
max_azul = canal_azul.max()
dicionario['Intensidad Minima'] = min_azul
dicionario['Intensidad Maxima'] = max_azul
promedio_canales = np.mean(imagen, axis=(0, 1))


dicionario = {'filas': filas, 
              'columnas' : columnas, 
              'canales' : canales, 
              'pixel_sup_izq' : pixelarribaizq,
              'pixel_sup_der' : pixelarribader,
              'pixel_inf_izq' :pixelabajoizq,
              'pixel_inf_der' : pixelabajoder, 
              'pixel_centro' : pixelcentro,
              'Intensidad Promedio' : promedio,
              'Intensidad Maxima': max_azul,
              'Intensidad Minima': min_azul,
              'color promedio canales': promedio_canales,
                }
for keys, val in dicionario.items():
    print(keys,val)
plt.show()
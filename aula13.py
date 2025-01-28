# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:27:44 2025

@author: 18798221728
"""

entrada = 'ossos.jpg'

import cv2
import numpy
import mfmv

imagem = cv2.imread(entrada)
cinza = mfmv.tonsCinza(imagem)
histCinza = mfmv.histograma(cinza, "grey")
mfmv.plotGraf(histCinza, 'grey', "tons de cinza")  


# matriz = numpy.zeros((10,10), dtype=int) #cria uma matriz toda preta
# matriz[1 , 6] = 255
# matriz[1 , 7] = 255
# matriz[1 , 8] = 255
# matriz[2 , 6] = 255
# matriz[2 , 7] = 255
# matriz[2 , 8] = 255
# matriz[3 , 5] = 255  
# matriz[3 , 6] = 255
# matriz[3 , 8] = 255
# matriz[4 , 5] = 255
# matriz[4 , 6] = 255  
# matriz[4 , 7] = 255
# matriz[4 , 8] = 255
# matriz[5 , 3] = 255
# matriz[5 , 4] = 255
# matriz[5 , 5] = 255  
# matriz[6 , 2] = 255
# matriz[6 , 3] = 255  
# matriz[6 , 4] = 255
# matriz[7 , 1] = 255
# matriz[7 , 4] = 255
# matriz[8 , 2] = 255  
# matriz[8 , 3] = 255
# matriz[8 , 4] = 255  


# imagemOriginal = matriz.astype(numpy.uint8)

# matriz_redimensionada = cv2.resize(matriz, (100, 100), interpolation=cv2.INTER_NEAREST)

# matriz_uint8 = matriz_redimensionada.astype(numpy.uint8)
# imagem = matriz_uint8

print('tamanho esperado:', (imagem.shape[1] * imagem.shape[0]))



mascara33 = numpy.full((3, 3), 1)

# mascara33 = numpy.array([[0, 1, 0],
#                     [1, 1, 1],
#                     [0, 1, 0]])

#--------------------------------------------------------------------------------------------------------#
#-----------------------------Aula 13: Extração de Componentes Conectados--------------------------------#
#--------------------------------------------------------------------------------------------------------#

PretoBranco = mfmv.limit(imagem, histCinza)
pb = mfmv.PBimg(cinza, 200)

posicao = mfmv.acharBuraco(PretoBranco)
print("posicao inicial ", posicao)

X = numpy.zeros_like(PretoBranco)
X[posicao] = 255

while True :
    XProx = mfmv.dilatacao(X, mascara33, 1)
    XProx = numpy.where((XProx == 255) & (PretoBranco == 255), 255, 0).astype(numpy.uint8)
    if numpy.array_equal(X, XProx):
        break
    X = XProx
    # cv2.imshow("X", X)
    # cv2.waitKey(0)

    
imagemFinal = X
   
cv2.imshow("imagem original", imagem)
cv2.imshow("imagem preta e branca", PretoBranco)
cv2.imshow("imagem pb", pb)

cv2.imshow("imagem final", imagemFinal)
cv2.waitKey(0)

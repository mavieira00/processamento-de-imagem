# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:09:29 2025

@author: 18798221728
"""
#entrada = 'homem.jpg'

import cv2
import numpy
import matplotlib.pyplot as plt
import mfmv

# imagem = cv2.imread(entrada)
# cinza = mfmv.tonsCinza(imagem)

# histCinza = mfmv.histograma(canalGrey, "grey")
# mfmv.plotGraf(histCinza, 'grey', "tons de cinza")

# print('tamanho esperado:', (imagem.shape[1] * imagem.shape[0]))

# # matriz = numpy.zeros((5,10), dtype=int) #cria uma matriz toda preta
# # matriz[1 , 3] = 255
# # matriz[2 , 3] = 255
# # matriz[1 , 9] = 255  
# # matriz[2 , 9] = 255

# # matriz_uint8 = matriz.astype(numpy.uint8)
# # #imagem = matriz_uint8

matriz = numpy.zeros((10,7), dtype=int) #cria uma matriz toda preta
matriz[1 , 2] = 255
matriz[1 , 3] = 255
matriz[2 , 1] = 255
matriz[2 , 4] = 255
matriz[3 , 1] = 255
matriz[3 , 4] = 255
matriz[4 , 2] = 255  
matriz[4 , 4] = 255
matriz[5 , 2] = 255
matriz[5 , 4] = 255
matriz[6 , 1] = 255  
matriz[6 , 5] = 255
matriz[7 , 1] = 255
matriz[7 , 5] = 255
matriz[8 , 1] = 255  
matriz[8 , 2] = 255
matriz[8 , 3] = 255  
matriz[8 , 4] = 255

imagemOriginal = matriz.astype(numpy.uint8)

matriz_redimensionada = cv2.resize(matriz, (490, 700), interpolation=cv2.INTER_NEAREST)

matriz_uint8 = matriz_redimensionada.astype(numpy.uint8)
imagem = matriz_uint8

print('tamanho esperado:', (imagem.shape[1] * imagem.shape[0]))
#numpy.random.seed(0)

mascara33 = numpy.full((3, 3), 1)

mascara33 = numpy.array([[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]])

#--------------------------------------------------------------------------------------------------------#
#-----------------------Aula 12: Extração de Fronteiras (Detecção de Contornos)--------------------------#
#--------------------------------------------------------------------------------------------------------#

# PretoBranco = mfmv.PBimg(imagem , 150)
# complemento = mfmv.inverterPB(PretoBranco)

# imagemErosionada = mfmv.erosao(PretoBranco, mascara33, 1)
# fronteira = PretoBranco - imagemErosionada

# cv2.imshow("imagem original", imagem)
# cv2.imshow("complemento", complemento)
# cv2.imshow("imagem preta e branca", PretoBranco)
# cv2.imshow("imagem apos erosao", imagemErosionada)
# cv2.imshow("fronteira", fronteira)
# cv2.waitKey(0) 


#--------------------------------------------------------------------------------------------------------#
#---------------------------------Aula 12: Preenchimento de Buracos--------------------------------------#
#--------------------------------------------------------------------------------------------------------#

PretoBranco = mfmv.PBimg(imagem , 150)
complemento = mfmv.inverterPB(PretoBranco)
matrizX = numpy.zeros((700,490), dtype=int) #cria uma matriz toda branca
matrizX[140 , 140] = 255
matriz_uint82 = matrizX.astype(numpy.uint8)
imagem2 = matriz_uint82

dila = mfmv.dilatacao(imagem2, mascara33, 1)
X1 = numpy.where((dila == 255) & (complemento == 255), 255, 0)
X1 = X1.astype(numpy.uint8)
print(X1.dtype)
print(X1.shape)


cv2.imshow("imagem original", imagemOriginal)
cv2.imshow("Matriz Redimensionada", imagem)
cv2.imshow("imagem preta e branca", PretoBranco)
cv2.imshow("complemento", complemento)
cv2.imshow("x0", imagem2)
cv2.imshow("dilatacao", dila)
cv2.imshow("x1", X1)
cv2.waitKey(0)



    

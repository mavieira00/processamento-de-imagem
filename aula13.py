# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:27:44 2025

@author: 18798221728
"""

import cv2
import numpy
import mfmv

# entrada = 'ossos.jpg'
# entrada = 'jEsq.jpg'
# imagem = cv2.imread(entrada)
# cinza = mfmv.tonsCinza(imagem)
# histCinza = mfmv.histograma(cinza, "grey")
# mfmv.plotGraf(histCinza, 'grey', "tons de cinza")  

matriz = numpy.array([
    [255, 255, 255, 255, 0, 0, 0],
    [255, 255, 255, 255, 0, 0, 0],
    [255, 255, 255, 255, 0, 0, 0],
    [255, 255, 255, 255, 255, 255, 255],
    [255, 255, 255, 255, 255, 255, 255],
    [255, 255, 255, 255, 255, 255, 255],
    [255, 255, 255, 255, 255, 255, 255]
]) 

cinza = imagem = matriz.astype(numpy.uint8)

# matriz_redimensionada = cv2.resize(matriz, (70, 70), interpolation=cv2.INTER_NEAREST)

# matriz_uint8 = matriz_redimensionada.astype(numpy.uint8)
# cinza = imagem = matriz_uint8


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



# mascara33 = numpy.full((3, 3), 1)

mascara33 = numpy.array([[0, 1, 0],
                    [1, 1, 1],
                    [0, 1, 0]])

#--------------------------------------------------------------------------------------------------------#
#-----------------------------Aula 13: Extração de Componentes Conectados--------------------------------#
#--------------------------------------------------------------------------------------------------------#

# PretoBranco = mfmv.PBimg(cinza, 180)

# posicao = mfmv.acharBuraco(PretoBranco)
# print("posicao inicial ", posicao)

# X = numpy.zeros_like(PretoBranco)
# X[posicao] = 255

# while True :
#     XProx = mfmv.dilatacao(X, mascara33, 1)
#     XProx = numpy.where((XProx == 255) & (PretoBranco == 255), 255, 0).astype(numpy.uint8)
#     if numpy.array_equal(X, XProx):
#         break
#     X = XProx
#     # cv2.imshow("X", X)
#     # cv2.waitKey(0)

    
# imagemFinal = X
   
# cv2.imshow("imagem original", imagem)
# cv2.imshow("imagem preta e branca", PretoBranco)
# cv2.imshow("imagem final", imagemFinal)
# cv2.waitKey(0)

#--------------------------------------------------------------------------------------------------------#
#--------------------------------------Aula 13: Esqueletização-------------------------------------------#
#--------------------------------------------------------------------------------------------------------#

PretoBranco = mfmv.PBimg(cinza, 150)

def esqueletizacao(imagem , e_estruturante, k):
    caveira = numpy.zeros((imagem.shape[0] , imagem.shape[1]), dtype=imagem.dtype)
    abertura1 = mfmv.abertura(imagem, e_estruturante, 1)
    diferenca1 = imagem - abertura1
    caveira = diferenca1
    
    while True:
        erosaok = mfmv.erosao(imagem, e_estruturante, k)
        print("erosao k")
        print(erosaok)
        aberturak = mfmv.abertura(erosaok, e_estruturante, 1)
        print("abertura k")
        print(aberturak)
        diferencak = erosaok - aberturak 
        print("diferença k")
        print(diferencak)
        
        caveira = numpy.maximum(caveira, diferencak)
        
        if numpy.all(aberturak == 0):
            break
        
        k = k + 1
    return caveira


caveira = esqueletizacao(PretoBranco, mascara33, 1)
inversao = mfmv.inverterPB(PretoBranco)
final = numpy.maximum(caveira, inversao)

cv2.imshow("imagem original", imagem)
cv2.imshow("imagem do esqueleto", caveira)
cv2.imshow("imagem final", final)
cv2.waitKey(0) 
    


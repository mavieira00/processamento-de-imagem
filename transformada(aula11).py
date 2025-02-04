# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:24:23 2025

@author: 18798221728
"""

#--------------------------------------------------------------------------------------------------------#
#--------------------------------Aula 11: hit-or-miss (encontrar padrões)--------------------------------#
#--------------------------------------------------------------------------------------------------------#

import cv2
import numpy
import matplotlib.pyplot as plt
import mfmv

matriz = numpy.zeros((200,200), dtype=int) #cria uma matriz toda preta

#coloca os quadrados tres por tres na matriz
matriz[11:14, 11:14] = 255
matriz[60:63, 80:83] = 255
matriz[145:148, 124:127] = 255  

# Adicionar um retângulo 15x25
matriz[20:35, 30:55] = 255

# Adicionar um retângulo 10x5
matriz[100:110, 50:55] = 255

# Adicionar um retângulo 25x40
matriz[120:145, 160:200] = 255

matriz_uint8 = matriz.astype(numpy.uint8)
imagem = matriz_uint8

print('tamanho esperado:', (imagem.shape[1] * imagem.shape[0]))
#numpy.random.seed(0)

PretoBranco = mfmv.PBimg(imagem, 150)

mascara33 = numpy.full((3, 3), 1)

erosao1 = mfmv.erosao(PretoBranco, mascara33, 1)
complemento1 = mfmv.inverterPB(PretoBranco)

engloba = mfmv.englobar_matriz(mascara33)

erosao2 = mfmv.erosao(complemento1, engloba, 1)
intersecao = numpy.where((erosao1 == 255) & (erosao2 == 255), 255, 0)

resultado = intersecao.copy()

coords = numpy.argwhere(intersecao == 255)

for coord in coords:
    x, y = coord
    N = mascara33.shape[0] // 2
    # Redimensionar o resultado para incluir a matrizest inteira no ponto indicado
    resultado[x-N:x + mascara33.shape[0] - N, y-N:y + mascara33.shape[1]-N] = mascara33
resultado = numpy.where((resultado == 1), 255, 0)
resultado = resultado.astype(numpy.uint8)

cv2.imshow("imagem original", imagem)
cv2.imshow("imagem após primeira erosao", erosao1)
cv2.imshow("imagem após segunda erosao", erosao2)
cv2.imshow("imagem apos complemento", complemento1)

#resultado = histograma.buscar_formas(BW, matrizest)
cv2.imshow("imagem apos operacao", resultado)
cv2.waitKey(0) 
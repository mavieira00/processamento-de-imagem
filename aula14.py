# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:24:45 2025

@author: 18798221728
"""

entrada = 'unhas.jpg'

import cv2
import numpy
import mfmv


imagem = cv2.imread(entrada)

canalCinza = mfmv.tonsCinza(imagem)

# mascara55 = numpy.full((5, 5), (1/5*5))

# mascara33 = numpy.full((3, 3), 1)

# mascara33 = numpy.array([[0, 1, 0],
#                     [1, 1, 1],
#                     [0, 1, 0]])

#--------------------------------------------------------------------------------------------------------#
#---------------------------------------------Aula 14: filtros-------------------------------------------#
#--------------------------------------------------------------------------------------------------------#

def mascara_media (tamanho):
    mascara = numpy.full((tamanho, tamanho), 1/tamanho**2)
    return mascara



bordas, imagem_suavizada = mfmv.convolucao(canalCinza, mascara_media(3) , 1)


    
cv2.imshow("imagem original", imagem)
cv2.imshow("imagem em tons de cinza", canalCinza)
cv2.imshow("imagem final", imagem_suavizada)
cv2.waitKey(0)
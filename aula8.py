# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:30:50 2024

@author: 18798221728
"""

entrada = 'digital2.jpg'

import cv2
import numpy
import matplotlib.pyplot as plt
import mfmv


imagem = cv2.imread(entrada)

canalGrey = mfmv.tonsCinza(imagem)
histCinza = mfmv.histograma(canalGrey, "grey")
mfmv.plotGraf(histCinza, 'grey', "tons de cinza")

print('tamanho esperado:', (imagem.shape[1] * imagem.shape[0]))

PretoBranco = mfmv.PBimg(canalGrey , 150)

#--------------------------------------------------------------------------------------------------------#
#---------------------------------------------Aula 8: erosão---------------------------------------------#
#--------------------------------------------------------------------------------------------------------#

#mascara 5x5
mascara55 = numpy.full((5, 5), (1/5*5))
#mascara 3x3
mascara33 = numpy.array([[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]])

resultado = mfmv.erosao(PretoBranco, mascara33, 1)

cv2.imshow("imagem original", canalGrey )
cv2.imshow("imagem erosionada", resultado)
cv2.waitKey(0) 
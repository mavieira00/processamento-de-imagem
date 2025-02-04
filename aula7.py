# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:52:09 2025

@author: 18798221728
"""

entrada = 'bolas.jpg'

import cv2
import numpy
import mfmv


imagem = cv2.imread(entrada)

canalCinza = mfmv.tonsCinza(imagem)

print('tamanho esperado:', (imagem.shape[1] * imagem.shape[0]))


mascara55 = numpy.full((5, 5), (1/5*5))

mascara33 = numpy.array([[0, 1, 0],
                         [1, -4, 1],
                         [0, 1, 0]])

#--------------------------------------------------------------------------------------------------------#
#-------------------------------------------Aula 7: Convolução-------------------------------------------#
#--------------------------------------------------------------------------------------------------------#

bordas, resultado = mfmv.convolucao(canalCinza, mascara55, 1)

print('tamanho da img orig: ', canalCinza.shape)
print('tamanho da img com bordas: ', bordas.shape)
print('tamanho da img convol: ', resultado.shape)


cv2.imshow("imagem original", canalCinza )
cv2.imshow("imagem com bordas", bordas)
cv2.imshow("imagem convolucionada", resultado)
#cv2.imshow("imagem expandida", img_expandida) #bom para usar com a imagem de neve
cv2.waitKey(0)
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:05:18 2025

@author: 18798221728
"""

entrada = 'digital.jpg'

import cv2
import numpy
import matplotlib.pyplot as plt
import mfmv


imagem = cv2.imread(entrada)
canalGrey = mfmv.tonsCinza(imagem)

histCinza = mfmv.histograma(canalGrey, "grey")
mfmv.plotGraf(histCinza, 'grey', "tons de cinza")

print('tamanho esperado:', (imagem.shape[1] * imagem.shape[0]))

pretoBranco = mfmv.PBimg(canalGrey , 150)
#--------------------------------------------------------------------------------------------------------#
#----------------------------------------Aula 10: abertura-----------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
#numpy.random.seed(0)

#mascara 5x5
mascara55 = numpy.full((5, 5), (1/5*5))
#mascara 3x3
mascara33 = numpy.array([[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]])

resultadoAbertura = mfmv.abertura(pretoBranco, mascara33, 1)
#resultadoErosao = mfmv.erosao(pretoBranco, mascara33, 1)
#resultadoAbertura = mfmv.dilatacao(resultadoErosao, mascara33, 1)


#--------------------------------------------------------------------------------------------------------#
#----------------------------------------Aula 10: fechamento---------------------------------------------#
#--------------------------------------------------------------------------------------------------------#

resultadoFechamento = mfmv.fechamento(pretoBranco, mascara33, 1)
#resultadoDilatacao = mfmv.dilatacao(pretoBranco, mascara33, 1)
#resultadoFechamento = mfmv.erosao(resultadoDilatacao, mascara33, 1)

resultadoFinal = mfmv.fechamento(resultadoAbertura, mascara33, 1)
#resultadoDila = mfmv.dilatacao(resultadoAbertura, mascara33, 1)
#resultadoFinal = mfmv.erosao(resultadoDila, mascara33, 1)

cv2.imshow("imagem original", canalGrey )
cv2.imshow("imagem PB", pretoBranco )
cv2.imshow("imagem abertura", resultadoAbertura )
cv2.imshow("imagem fechamento", resultadoFechamento )
cv2.imshow("fechamento da abertura", resultadoFinal)
cv2.waitKey(0) 
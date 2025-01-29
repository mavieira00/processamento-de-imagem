# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:09:29 2025

@author: 18798221728
"""
entrada = 'homem.jpg'

import cv2
import numpy
import mfmv

imagem = cv2.imread(entrada)
cinza = mfmv.tonsCinza(imagem)

print('tamanho esperado:', (imagem.shape[1] * imagem.shape[0]))

# matriz = numpy.zeros((5,10), dtype=int) #cria uma matriz toda preta
# matriz[1 , 3] = 255
# matriz[2 , 3] = 255
# matriz[1 , 9] = 255  
# matriz[2 , 9] = 255

# matriz_uint8 = matriz.astype(numpy.uint8)
# imagem = matriz_uint8

# matriz = numpy.zeros((10,7), dtype=int) #cria uma matriz toda preta
# matriz[1 , 2] = 255
# matriz[1 , 3] = 255
# matriz[2 , 1] = 255
# matriz[2 , 4] = 255
# matriz[3 , 1] = 255
# matriz[3 , 4] = 255
# matriz[4 , 2] = 255  
# matriz[4 , 4] = 255
# matriz[5 , 2] = 255
# matriz[5 , 4] = 255
# matriz[6 , 1] = 255  
# matriz[6 , 5] = 255
# matriz[7 , 1] = 255
# matriz[7 , 5] = 255
# matriz[8 , 1] = 255  
# matriz[8 , 2] = 255
# matriz[8 , 3] = 255  
# matriz[8 , 4] = 255

# imagemOriginal = matriz.astype(numpy.uint8)

# matriz_redimensionada = cv2.resize(matriz, (70, 100), interpolation=cv2.INTER_NEAREST)

# matriz_uint8 = matriz_redimensionada.astype(numpy.uint8)
# imagem = matriz_uint8

# print('tamanho esperado:', (imagem.shape[1] * imagem.shape[0]))
# numpy.random.seed(0)

# mascara33 = numpy.full((3, 3), 1)

mascara33 = numpy.array([[0, 1, 0],
                    [1, 1, 1],
                    [0, 1, 0]])

#--------------------------------------------------------------------------------------------------------#
#-----------------------Aula 12: Extração de Fronteiras (Detecção de Contornos)--------------------------#
#--------------------------------------------------------------------------------------------------------#

PretoBranco = mfmv.PBimg(cinza , 150)
complemento = mfmv.inverterPB(PretoBranco)

imagemErosionada = mfmv.erosao(PretoBranco, mascara33, 1)
fronteira = PretoBranco - imagemErosionada

cv2.imwrite("saida.jpg", fronteira)
# cv2.imshow("imagem original", imagem)
# cv2.imshow("complemento", complemento)
# cv2.imshow("imagem preta e branca", PretoBranco)
# cv2.imshow("imagem apos erosao", imagemErosionada)
# cv2.imshow("fronteira", fronteira)
# cv2.waitKey(0) 


#--------------------------------------------------------------------------------------------------------#
#---------------------------------Aula 12: Preenchimento de Buracos--------------------------------------#
#--------------------------------------------------------------------------------------------------------#

PretoBranco = mfmv.PBimg(fronteira , 150)

posicao = mfmv.acharBuraco(PretoBranco)
print("posicao inicial ", posicao)

complemento = mfmv.inverterPB(PretoBranco)

X = numpy.zeros_like(PretoBranco)
X[posicao] = 255

while True :
    XProx = mfmv.dilatacao(X, mascara33, 1)
    XProx = numpy.where((XProx == 255) & (complemento == 255), 255, 0).astype(numpy.uint8)
    if numpy.array_equal(X, XProx):
        break
    X = XProx
    # cv2.imshow("X", X)
    # cv2.waitKey(0)

    
imagemFinal = X + PretoBranco
   
cv2.imshow("imagem original", imagem)
cv2.imshow("imagem preta e branca", PretoBranco)
cv2.imshow("complemento", complemento)
cv2.imshow("X", X)
cv2.imshow("imagem final", imagemFinal)
cv2.waitKey(0)



    

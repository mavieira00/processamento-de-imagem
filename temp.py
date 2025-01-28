nomeImagem = 'teste.jpg'

import cv2
import numpy 
import matplotlib.pyplot as plt
import mfmv

imagem = cv2.imread(nomeImagem)

print ('largura em pixels: ', end='')
print (imagem.shape[1])

print ('altura em pixels: ', end='')
print (imagem.shape[0])

print ('quantidade de canais: ', end='')
print (imagem.shape[2])

canalGrey = mfmv.tonsCinza(imagem)
histCinza = mfmv.histograma(canalGrey, "grey")
mfmv.plotGraf(histCinza, 'grey', "tons de cinza")  

# histb = mfmv.histograma(imagem[:,:,0], "blue")
# mfmv.plotGraf(histb, 'blue', "tons de azul")

# histg = mfmv.histograma(imagem[:,:,1], "green")
# mfmv.plotGraf(histg, 'green', "tons de verde")

# histr = mfmv.histograma(imagem[:,:,2], "red")
# mfmv.plotGraf(histr, 'red', "tons de vermelho")

cv2.imshow("preto", mfmv.limit(imagem, histCinza))
cv2.imshow("branco", mfmv.limit2(imagem, histCinza))
# cv2.imshow("colorida", imagem)
# cv2.imshow("cinza", canalGrey)
# cv2.imshow("vermelha", canalRed)
# cv2.imshow("verde", canalGreen)
# cv2.imshow("azul", canalBlue)
# cv2.waitKey(0)

#cv2.imwrite("saida.jpg", imagem)
# def curvaTom(canal, ctrs, lumi):
#     imagemAlterada = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
#     for i in range(imagemAlterada.shape[0]):
#         for j in range(imagemAlterada.shape[1]):
#             s = ((canal[i][j]*ctrs) + lumi)
#             if(s > 255):
#                 s = 255
#             imagemAlterada[i,j] = s    
#     return (imagemAlterada)
# imagemAlterada = curvaTom(canalGrey, 2, 0)
# mfmv.plotFuncao(2, 0)
# histAlt = mfmv.histograma(imagemAlterada, "pink")
# mfmv.plotGraf(histAlt, 'pink', "alteração")

# def curvaTomNeg(canal, ctrs, lumi):
#     imagemAlterada = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
#     for i in range(imagemAlterada.shape[0]):
#         for j in range(imagemAlterada.shape[1]):
#             s = 255 - ((canal[i][j]*ctrs) + lumi)
#             if(s > 255):
#                 s = 255
#             imagemAlterada[i,j] = s    
#     return (imagemAlterada)
# imagemNeg = curvaTomNeg(canalGrey, 1, 0)
# mfmv.plotFuncaoNeg(1, 0)
# histNeg = mfmv.histograma(imagemNeg, "yellow")
# mfmv.plotGraf(histNeg, 'yellow', "negativo")

# def curvaTomPara(canal):
#     imagemAlterada = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
#     for i in range(imagemAlterada.shape[0]):
#         for j in range(imagemAlterada.shape[1]):
#             s = (((1/256)*canal[i][j])**2) *255
#             # if(s > 255):
#             #     s = 255
#             imagemAlterada[i,j] = s    
#     return (imagemAlterada)
# imagemPara = curvaTomPara(canalGrey)
# mfmv.plotFuncaoPara()
# histPara = mfmv.histograma(imagemPara, "orange")
# mfmv.plotGraf(histPara, 'orange', "parabólica")

# def expansao(canal, r1, r2):
#     imagemContraste = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
#     for i in range(imagemContraste.shape[0]):
#         for j in range(imagemContraste.shape[1]):
#             r = canal[i][j]
#             if(r1 <= r & r <= r2):
#                 s = 255 * ((r-r1)/(r2-r1))
#             elif(r <= r1):
#                 s = 0
#             else:
#                 s = 255
#             imagemContraste[i][j] = s
#     return (imagemContraste)

# imagemContr = expansao(canalGrey, 100, 130)
# histContr = mfmv.histograma(imagemContr, "black")
# mfmv.plotGraf(histContr, 'black', "expansão")

# def norma(imagem):
#     total = imagem.shape[1]*imagem.shape[0]
#     prob =  [0]*256
#     hist = numpy.zeros(256, dtype = numpy.uint) #hist = [0]*256
#     for i in range(imagem.shape[0]):
#         for j in range(imagem.shape[1]):
#             hist[imagem[i][j]] += 1;
            
#     for i in range(256):
#        prob[i] = hist[i]/total
#     return(prob)         
# histNorma = norma(canalGrey)
# mfmv.plotGraf(histNorma, 'black', "da imagem normalizada")      

# def normaAcumu(hist):
#     soma = 0
#     histograma = [0]*256
#     for i in range(256):
#         soma += hist[i]
#         histograma[i] = soma
#     print('soma: ', end='')
#     print(soma)
#     return(histograma)
# histAcumu = normaAcumu(histNorma)   
# mfmv.plotGraf(histAcumu, 'pink', "acumulado da normalizada") 

# def mapeamento(hist):
#     mapa = [0]*256
#     #imagemAlterada = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
#     for i in range(256):
#         #var = round(hist[i]*255)
#         mapa[i] = int(round(hist[i]*255))
#     print(mapa)
#     return mapa
# mapa1 = mapeamento(histAcumu)

# def equalizado(canal, mapa):
#     imagemAlterada = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
#     for i in range(imagemAlterada.shape[0]):
#         for j in range(imagemAlterada.shape[1]):
#             imagemAlterada[i][j] = mapa[canal[i][j]]
#     return (imagemAlterada)

# imagemEqualizada = equalizado(canalGrey, mapa1)
# histEquali = mfmv.histograma(imagemEqualizada, "orange")
# mfmv.plotGraf(histEquali, 'orange', "equalizada")

# def histEsp(imagem):
#     hist = [0]*256
#     for i in range(256):
#         hist[i] = pow(i - 127, 2)
#         #hist[i] = i
        
#     hist /= numpy.sum(hist)  # Normalização para que a soma seja 1
#     #print (hist)
#     return hist

# histEspe = histEsp(canalGrey)
# mfmv.plotGraf(histEspe, 'purple', "especifico")   
# espAcumu = normaAcumu(histEspe)  
# mfmv.plotGraf(espAcumu, 'pink', "acumulado")  

# mapa2 = mapeamento(espAcumu)




# #imagemEqualizada2 = equalizado(imagemEqualizada, espAcumu)
# #histEqualiEsp = mfmv.histograma(imagemEqualizada2, "orange")
# #mfmv.plotGraf(histEqualiEsp, 'orange', "equalizada2")
   

# cv2.imshow("alterada", imagemAlterada)
# cv2.imshow("negativa", imagemNeg)
#cv2.imshow("parabolica", imagemPara)
cv2.imshow("cinza", canalGrey)
#cv2.imshow("equalizada", imagemEqualizada)
#cv2.imshow("equalizada 2", imagemEqualizada2)
#cv2.imshow("expandida", imagemContr)
cv2.waitKey(0)
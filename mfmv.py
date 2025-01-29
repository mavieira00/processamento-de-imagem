# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:24:40 2024

@author: mavi
"""
import numpy
import matplotlib.pyplot as plt
import cv2

def tonsCinza(imagem):
    canalBlue = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8)
    canalGreen = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8)
    canalRed = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8)
    canalGrey = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)

    canalBlue[:,:,0] = imagem[:,:,0]
    canalGreen [:,:,1] = imagem[:,:,1]
    canalRed [:,:,2] = imagem[:,:,2]

    for i in range(canalGrey.shape[0]):
        for j in range(canalGrey.shape[1]):
               #canalGrey[i][j] = (imagem[i][j].sum()//3) # // garante resultado inteiro
               canalGrey[i,j] = (canalBlue[i,j,0]//3) + (canalGreen[i,j,1]//3) + (canalRed[i,j,2]//3)
               #canalGrey[i,j] = (canalBlue[i,j,0] + canalGreen[i,j,1] + canalRed[i,j,2])//3 # OVER
    return canalGrey

def histograma(imagem, color):
    hist = numpy.zeros(256, dtype = numpy.uint) #hist = [0]*256
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            hist[imagem[i][j]] += 1;
    return(hist)


def plotGraf(histograma, cor, cor2):
    pixel = 256*[0]
    for i in range(256):
        pixel[i] = i
    plt.xlabel('pixel')
    plt.ylabel('quantidade')
    plt.title(f'histograma {cor2}')
    plt.bar(pixel, histograma, color=cor)
    plt.show()
    
def limit(imagem, hist):
    canalPreto = tonsCinza(imagem)
    k = 150
    for i in range(canalPreto.shape[0]):
        for j in range(canalPreto.shape[1]):
            if(canalPreto[i][j] > k):
                canalPreto[i][j] = 255
    return(canalPreto)

def limit2(imagem, hist):
    canalBranco = tonsCinza(imagem)
    k = 150
    for i in range(canalBranco.shape[0]):
        for j in range(canalBranco.shape[1]):
            if(canalBranco[i][j] < k):
                canalBranco[i][j] = 255
    return(canalBranco)

def limitMulti(imagem, hist):
    canalBranco = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
    canalGrey = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
    for i in range(imagem.shape[1]):
        for j in range(imagem.shape[0]):
               canalGrey[i][j] = (imagem[i][j].sum()//3) # // garante resultado inteiro
               canalBranco[i,j] = (imagem[i][j].sum()//3)
    k = 150
    for i in range(canalBranco.shape[0]):
        for j in range(canalBranco.shape[1]):
            if(canalBranco[i][j] < k):
                canalBranco[i][j] = 255
    return(canalBranco)


    
def plotFuncao(ctrs,lumi):
    x = numpy.arange(0, 256)
    y = (x * ctrs) + lumi
    y = numpy.clip(y, 0, 255)
    plt.plot(x, y, label=f'f(x) = {ctrs} * x + {lumi}')
    plt.xlabel('origem: -r')
    plt.ylabel('destino: -s')
    plt.title('curva de tom do brilho e contraste')
    plt.grid(True)
    plt.show()
    
def plotFuncaoNeg(ctrs,lumi):
    x = numpy.arange(0, 256)
    y = 255 - (x * ctrs) + lumi
    y = numpy.clip(y, 0, 255)
    plt.plot(x, y, label=f'f(x) = {ctrs} * x + {lumi}')
    plt.xlabel('origem: -r')
    plt.ylabel('destino: -s')
    plt.title('curva de tom do negativo da imagem original')
    plt.grid(True)
    plt.show()
    
def plotFuncaoPara():
    x = numpy.arange(0, 256)
    y = ((1/256)*x)**2
    y = numpy.clip(y, 0, 255)
    plt.plot(x, y, label=f'f(x) = ((1/256)*x)**2')
    plt.xlabel('origem: -r')
    plt.ylabel('destino: -s')
    plt.title('curva de tom Parabólica')
    plt.grid(True)
    plt.show()
    
def PBimg(imagemCinza, corte):
    PBimg = imagemCinza.copy()
    for i in range(PBimg.shape[0]):
        for j in range(PBimg.shape[1]):
            if  PBimg[i][j] < corte:
               PBimg[i][j] = 0
            if  PBimg[i][j] >= corte:
               PBimg[i][j] = 255
    return PBimg

def erosao(imagem, mascara, n): #n = n de repetições na convolucao
    #adicionar borda:
    tamanho_matriz = mascara.shape[0]
    
    borda = (tamanho_matriz - 1) // 2
    while(n>0):
        
        
        #bordas devem ser +2 em matriz 3x3 e + 4 em matriz 5x5 (ou seja, sempre aumenta em 2 o valor)
        imagem_com_bordas = numpy.full((imagem.shape[0] + 2 * borda, imagem.shape[1] + 2 * borda), 255, dtype=imagem.dtype)
        #deve ser -1 em matriz 3x3 e -2 em matriz 5x5 (ou seja, sempre diminui em 1 o valor)
        imagem_com_bordas[borda:-borda, borda:-borda] = imagem
        # Obter as dimensões da imagem e da máscara
        imagem_altura, imagem_largura = imagem.shape
        mascara_altura, mascara_largura = mascara.shape
            
        # Matriz de saída
        imagem_erosionada = numpy.zeros_like(imagem, dtype = numpy.uint8)  
        
        
        for i in range(imagem_altura):
            for j in range(imagem_largura):
                # Extrair a submatriz da imagem que corresponde à máscara
                submatriz = imagem_com_bordas[i:i + mascara_altura, j:j + mascara_largura]
                
                if numpy.all(submatriz[mascara == 1] == 255):
                    imagem_erosionada[i , j] = 255
                else:
                    imagem_erosionada[i , j] = 0
        
        imagem = imagem_erosionada.copy()
        n = n-1
    return imagem_erosionada

def dilatacao(imagem, mascara, n): #n = n de repetições na convolucao
    while(n>0):
        
        #adicionar borda:
        tamanho_matriz = mascara.shape[0]
    
        borda = (tamanho_matriz - 1) // 2
        #bordas devem ser +2 em matriz 3x3 e + 4 em matriz 5x5 (ou seja, sempre aumenta em 2 o valor)
        imagem_com_bordas = numpy.zeros((imagem.shape[0] + 2 * borda, imagem.shape[1] + 2 * borda), dtype=imagem.dtype)
        #deve ser -1 em matriz 3x3 e -2 em matriz 5x5 (ou seja, sempre diminui em 1 o valor)
        imagem_com_bordas[borda:-borda, borda:-borda] = imagem
        # Obter as dimensões da imagem e da máscara
        imagem_altura, imagem_largura = imagem.shape
        mascara_altura, mascara_largura = mascara.shape
            
        # Matriz de saída
        imagem_dilatada = numpy.zeros_like(imagem, dtype = numpy.uint8)  
        
        
        for i in range(imagem_altura):
            for j in range(imagem_largura):
                # Extrair a submatriz da imagem que corresponde à máscara
                submatriz = imagem_com_bordas[i:i + mascara_altura, j:j + mascara_largura]
                
                if numpy.any(submatriz[mascara == 1] == 255 ):
                    imagem_dilatada[i , j] = 255
                else:
                    imagem_dilatada[i , j] = 0
        
        imagem = imagem_dilatada.copy()
        n = n-1
    return imagem_dilatada


def inverterPB(imagemPB):
    PBimg = imagemPB.copy()
    PBimg = numpy.where(PBimg == 0, 255, numpy.where(PBimg == 255, 0, PBimg))
    return PBimg

def englobar_matriz(mascara):
    N = mascara.shape[0]  # Tamanho da mascara
    # Criar uma matriz de tamanho (N+2) x (N+2) preenchida com 1
    mascara2 = numpy.ones((N+2, N+2), dtype=int)
    # Substituir os valores de dentro por 0
    mascara2[1:N+1, 1:N+1] = 0
    return mascara2

def abertura(imagem , mascara, n):
    erosaoA = erosao(imagem, mascara, n)
    abertura = dilatacao(erosaoA, mascara, n)
    return abertura

def fechamento(imagem , mascara, n):
    dilatacaoF = dilatacao(imagem, mascara, n)
    fechamento = erosao(dilatacaoF, mascara, n)
    return fechamento

def acharBuraco(imagem):
    linha = len(imagem)
    coluna = len(imagem[0])
    
    for i in range(1, linha):
        for j in range(1, coluna):
            if (imagem[i][j] == 0 and imagem[i-1][j] == 255 and  imagem[i][j-1] == 255):
                return (i, j)
    
    return None
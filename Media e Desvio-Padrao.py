# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 18:12:37 2022

@author: GRCav
"""

import numpy as np
import pickle

unpickleFile = open('C:\\Users\\GRCav\\OneDrive\\Documentos\\dados.pkl', 'rb')  #Abre o arquivo 'file' criado anteriormente
new_dados = pickle.load(unpickleFile, encoding = 'bytes')  #Cria uma variável 'new_dados' que permite usar os dados do arquivo
   
x = new_dados.keys()  #Cria uma variável que usa os arquivos 'edf' e os eletrodos
for i in x:  #Itera a variável 'x'
    I = new_dados[i]  #Cria uma variável que grava os sinais de cada eletrodo 'i'
    n = 0  #Cria uma variável em branco 'n'
    N = 0  #Cria uma variável em branco 'N'
    for t in range(len(I[0])):  #Itera os sinais de cada eletrodo
        n += I[0][t]  #Soma dos sinais
        N += 1  #Soma da quantidade de sinais
    X = n/N  #Cálculo da média dos sinais
    S = np.sqrt((n-X)**2/(N-1))  #Cálculo do desvio-padrão dos sinais
    print(X, S)
    
    
    archive = open('C:\\Users\\GRCav\\OneDrive\\Documentos\\M-DP.pkl', 'wb')  #Cria e abre um arquivo pkl
    pickle.dump(X, archive)  #Grava a média no arquivo 'archive'
    pickle.dump(S, archive)  #Grava o desvio-padrão no arquivo 'archive'
    archive.close()  #Fecha o arquivo 'archive'
    
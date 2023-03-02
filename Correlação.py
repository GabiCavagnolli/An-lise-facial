# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 16:42:58 2022

@author: GRCav
"""

import pandas as pd
import numpy as np
import pickle

unpickleFile = open('C:\\Users\\GRCav\\OneDrive\\Documentos\\dados.pkl', 'rb')  #Abre o arquivo 'archive' criado anteriormente
new_dados = pickle.load(unpickleFile, encoding = 'bytes')  #Cria uma variável 'new_dados' que permite usar os dados do arquivo

x = list(new_dados.keys())  #Cria uma variável contendo uma lista com os dados do 'edf'

EEG_channels =  ['Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T7', 'T8', 'P7','P8', 'Fz', 'Cz', 'Oz', 'FC1', 'FC2', 'CP1', 'CP2', 'FC5', 'FC6', 'CP5', 'CP6', 'TP9', 'TP10', 'POz']  #Cria uma lista com o nome de todos os eletrodos utilizados no eletroencefalograma         
x[0][1] in EEG_channels  #Comprovação de que os dados da lista 'EEG_channels' estão na lista 'x'

b = 'sub-01_eeg_sub-01_task-classicalMusic_eeg.edf'  #Cria uma variável com o nome do arquivo
c = 'sub-01_eeg_sub-01_task-genMusic01_eeg.edf'  #Cria uma variável com o nome do arquivo
d = 'sub-01_eeg_sub-01_task-genMusic02_eeg.edf'  #Cria uma variável com o nome do arquivo
e = 'sub-01_eeg_sub-01_task-genMusic03_eeg.edf'  #Cria uma variável com o nome do arquivo
f = 'sub-01_eeg_sub-01_task-washout_eeg.edf'  #Cria uma variável com o nome do arquivo

df = pd.DataFrame()  #Cria uma variável contendo uma tabela em branco


for a in range(len(x)):  #Itera os números da lista 'x'
    if x[a][1] in EEG_channels:  #Se o eletrodo correspondente a 'a' está no 'EEG_channels'
        if x[a][0] == b:  #Se o arquivo do eletrodo corresponte a 'a' é igual a variável b
            sinal = new_dados[x[a]]  #Cria uma variável com os sinais do eletrodo correspondente a 'a'
            corr = np.corrcoef(sinal, new_dados[x[31]])[0, 1]   #Cria uma variável contendo a correlação do sinal do eletrodo correspondente a 'a' e ECG
            print(a)  #Mostra o número de 'a'
            print(corr)  #Mostra a correlação
            channels = pd.DataFrame({'Arquivo': [b], x[a][1]: [corr]})  #Cria uma variável com a linha 'arquivo' e uma coluna com a correlação do eletrodo correspondente a 'a'
        elif x[a][0] == c:   #Se o arquivo do eletrodo corresponte a 'a' é igual a variável c
            sinal = new_dados[x[a]]  #Cria uma variável com os sinais do eletrodo correspondente a 'a'
            corr = np.corrcoef(sinal, new_dados[x[78]])[0, 1]   #Cria uma variável contendo a correlação do sinal do eletrodo correspondente a 'a' e ECG
            print(a)  #Mostra o número de 'a'
            print(corr)    #Mostra a correlação
            channels = pd.DataFrame({'Arquivo': [c], x[a][1]: corr})  #Cria uma variável com a linha 'arquivo' e uma coluna com a correlação do eletrodo correspondente a 'a'
        elif x[a][0] == d:  #Se o arquivo do eletrodo corresponte a 'a' é igual a variável d
            sinal = new_dados[x[a]]  #Cria uma variável com os sinais do eletrodo correspondente a 'a'
            corr = np.corrcoef(sinal, new_dados[x[125]])[0, 1]   #Cria uma variável contendo a correlação do sinal do eletrodo correspondente a 'a' e ECG
            print(a)  #Mostra o número de 'a'
            print(corr)  #Mostra a correlação
            channels = pd.DataFrame({'Arquivo': [d], x[a][1]: corr})  #Cria uma variável com a linha 'arquivo' e uma coluna com acorrelação do eletrodo correspondente a 'a'
        elif x[a][0] == e:  #Se o arquivo do eletrodo corresponte a 'a' é igual a variável e
            sinal = new_dados[x[a]]  #Cria uma variável com os sinais do eletrodo correspondente a 'a'
            corr = np.corrcoef(sinal, new_dados[x[172]])[0, 1]   #Cria uma variável contendo a correlação do sinal do eletrodo correspondente a 'a' e ECG
            print(a)  #Mostra o número de 'a'
            print(corr)  #Mostra a correlação
            channels = pd.DataFrame({'Arquivo': [e], x[a][1]: corr})  #Cria uma variável com a linha 'arquivo' e uma coluna com acorrelação do eletrodo correspondente a 'a'
        elif x[a][0] == f:  #Se o arquivo do eletrodo corresponte a 'a' é igual a variável f
            sinal = new_dados[x[a]]  #Cria uma variável com os sinais do eletrodo correspondente a 'a'
            corr = np.corrcoef(sinal, new_dados[x[219]])[0, 1]   #Cria uma variável contendo a correlação do sinal do eletrodo correspondente a 'a' e ECG
            print(a)  #Mostra o número de 'a'
            print(corr)  #Mostra a correlação
            channels = pd.DataFrame({'Arquivo': [f], x[a][1]: corr})  #Cria uma variável com a linha 'arquivo' e uma coluna com acorrelação do eletrodo correspondente a 'a'
            
        df = pd.concat([df, channels])  #Junta todas as linhas e colunas 
        
print(df)  #Mostra a tabela criada
         
         

"""
Tabela
coluna = eletrodo
linha = arquivo
"""


         
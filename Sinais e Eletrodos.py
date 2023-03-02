# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 12:10:16 2022

@author: GRCav
"""

import matplotlib.pyplot as plt
from pyedflib import highlevel
import pickle
    
import os
arquivo = os.listdir('C:\\Users\\GRCav\\OneDrive\\Documentos\\Dataset\\sub-01\\eeg')  #Abrindo a pasta necessário de um eletroencefalograma
print(arquivo[0][-3:])  #Mostrar só as 3 últimas letras do nome do arquivo que será usado (edf)



dados = dict()  #Criando um dicionário em branco
for i in arquivo:  #Iterando a pasta aberta anteriormente
    e = 'C:\\Users\\GRCav\\OneDrive\\Documentos\\Dataset\\sub-01\\eeg\\' + i  #Criando uma variável onde junta a localização da pasta com os arquivos iterados da pasta
    print(i)  #Mostra cada arquivo iterado 'i'
    if e[-3:] == 'edf':  #Se a variável e tiver as três últimas letra 'edf' (um arquivo com dados de muilticanais biologicos e sinais físicos)
            info = highlevel.read_edf_header(e, read_annotations=True)  #Criando uma varável que lê o arquivo 'e' 'edf' e seus sinais
            
            for c in info['channels']: #Itera os eletrodos da variavel 'info' anteriormente criada
                print(c)  #Mostra cada eletrodo iterado 'c'
                signals, signal_headers, header = highlevel.read_edf(e, ch_names = c)  #Cria variáveis para os sinais dos arquivos 'edf'
                plt.figure()  #Cria gráficos
                plt.plot(signals.T)  #Coloca os sinais como dados dos gráficos
                plt.xlabel(c)  #Coloca o eletrodo 'c' iterado como nome do eixo x
                plt.ylabel(i)  #Coloca o arquivo 'i' iterado como nome do eixo y
                plt.show()  #Mostra os gráficos
                dados[i, c] = signals  #Grava os sinais do arquivo 'i' iterado e o eletrodo 'c' iterado

file = open('C:\\Users\\GRCav\\OneDrive\\Documentos\\dados.pkl', 'wb')  #Cria e abre um arquivo em pkl
pickle.dump(dados, file)  #Grava os dados com os sinais e eletrodos no arquivo 'file' criado
file.close()  #Fecha o arquivo 'file'
                
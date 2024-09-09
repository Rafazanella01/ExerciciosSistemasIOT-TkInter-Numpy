import pandas as pd
import numpy as np
from tkinter import *
from tkinter import filedialog, Label
import matplotlib.pyplot as plt


def meancenter(matriz):
    
    media = np.mean(matriz, axis=0)
    
    out = matriz - media
    
    return out

def autoscale(dados):
    media = np.mean(dados, axis=0)
    desvioPadrao = np.std(dados, axis=0)
    
    dadosEscalados = (dados - media) / desvioPadrao
    
    return dadosEscalados

def plotarGraficos():
    matriz = root.matriz
    matrizCentrada = root.matrizCentrada
    matrizEscalada = root.matrizEscalada
    fig, axs = plt.subplots(3, 1, figsize=(10, 15))

    axs[0].plot(matriz)
    axs[0].set_title('Dados Originais', pad=0)  
    axs[1].set_title('Mean Center', pad=0)

    axs[2].plot(matrizEscalada)
    axs[2].set_title('Auto Scale', pad=0)

    plt.subplots_adjust(hspace=0.5) 

    plt.tight_layout()
    plt.show()

def mostrarMatriz(widget, matriz, titulo):
    widget.delete(1.0, END)  
    widget.insert(END, f"{titulo}:\n")
    for linha in matriz:
        widget.insert(END, ' '.join(map(str, linha)) + "\n")

def selecionarArquivo():
    arquivo = filedialog.askopenfilename(
        title= "Selecione o arquivo CSV",
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*"))
    )
    
    if arquivo:
        matriz = pd.read_csv(arquivo).values  # Lê o CSV em uma matriz numpy
        matrizCentrada = meancenter(matriz)
        matrizEscalada = autoscale(matriz)
        
        mostrarMatriz(texto_matriz_centrada, matrizCentrada, "Matriz Centragem pela Média")
        mostrarMatriz(texto_matriz_escalada, matrizEscalada, "Matriz Autoscale")
        
        botao_gerar_graficos.pack(pady=10)

        root.matriz = matriz
        root.matrizCentrada = matrizCentrada
        root.matrizEscalada = matrizEscalada        
        #plotarGraficos(matriz, matrizCentrada, matrizEscalada)

root = Tk()

botao = Button(root, text="Selecione um arquivo", command=selecionarArquivo)
botao.pack(pady=20)

texto_matriz_centrada = Text(root, height=10, width=50)
texto_matriz_centrada.pack(pady=10)

texto_matriz_escalada = Text(root, height=10, width=50)
texto_matriz_escalada.pack(pady=10)

botao_gerar_graficos = Button(root, text="Gerar Gráficos", command=plotarGraficos)
botao_gerar_graficos.pack_forget()

root.mainloop()
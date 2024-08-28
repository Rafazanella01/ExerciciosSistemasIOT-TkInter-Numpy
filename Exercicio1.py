import pandas as pd
import numpy as np

def meancenter(matriz):
    
    media = np.mean(matriz, axis=0)
    
    out = matriz - media
    
    return out

def autoscale(dados):
    media = np.mean(dados, axis=0)
    desvioPadrao = np.std(dados, axis=0)
    
    dadosEscalados = (dados - media) / desvioPadrao
    
    return dadosEscalados
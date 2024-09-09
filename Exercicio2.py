import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from dateutil.relativedelta import relativedelta

def calcularIdade():
    try:
        dataNascimento = datetime.strptime(entryData.get(), "%d/%m/%Y")
        dataAtual = datetime.now()
        
        diferenca = relativedelta(dataAtual, dataNascimento)
        
        resultado = f"{diferenca.years} anos, {diferenca.months} meses e {diferenca.days} dias"
        labelResultado.config(text="Resultado: " + resultado)
    except ValueError:
        messagebox.showerror("Erro", "Formato de data inválido. Use DD/MM/AAAA.")

janela = tk.Tk()
janela.title("Calculadora de Idade")

labelTexto = tk.Label(janela, text="Digite o ano de nascimento:", font=("Arial", 14))
labelTexto.pack(pady=10)

entryData = tk.Entry(janela, font=("Arial", 14))
entryData.pack(pady=10)

botaoCalcular = tk.Button(janela, text="Calcular", font=("Arial", 14), command=calcularIdade)
botaoCalcular.pack(pady=10)

labelResultado = tk.Label(janela, text="", font=("Arial", 16), fg="yellow", bg="black")
labelResultado.pack(pady=20)

janela.mainloop()

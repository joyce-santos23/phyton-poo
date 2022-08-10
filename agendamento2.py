from optparse import Values
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from turtle import bgcolor

oJanelaAgendamento = tk.Tk()
oJanelaAgendamento.title("Sistema de Gerenciamento de Exames")
oJanelaAgendamento.geometry("1000x700")
oJanelaAgendamento.configure(background="#C0C0C0")

#Definição label tela de Agendamento
Titulofont = tkFont.Font(family="Lucida Grande", size=15)
Titulo = tk.Label(oJanelaAgendamento, text="SISTEMA DE GERENCIAMENTO DE EXAMES", bg="#C0C0C0", fg="#000000", font=Titulofont)
lbMatricula = tk.Label(oJanelaAgendamento, text='Matrícula:', bg="#C0C0C0", fg="#000000")
lbNome = tk.Label(oJanelaAgendamento, text='Nome:', bg="#C0C0C0", fg="#000000")
cbExame = tk.Label(oJanelaAgendamento, text='Exame:', bg="#C0C0C0", fg="#000000")
cbComplementar = tk.Label(oJanelaAgendamento, text='Complementar:', bg="#C0C0C0", fg="#000000")
lbClinica = tk.Label(oJanelaAgendamento, text='Clínica:', bg="#C0C0C0", fg="#000000")
lbCidade = tk.Label(oJanelaAgendamento, text='Cidade:', bg="#C0C0C0", fg="#000000")
lbUF = tk.Label(oJanelaAgendamento, text='UF:', bg="#C0C0C0", fg="#000000")

#Localização dos campos label da tela de Agendamento
Titulo.place(relx=0.35, rely=0.1)
lbMatricula.place(relx=0.38, rely=0.20)
lbNome.place(relx=0.38, rely=0.25)
cbExame.place(relx=0.38, rely=0.30)
cbComplementar.place(relx=0.38, rely=0.35)
lbClinica.place(relx=0.38, rely=0.40)
lbCidade.place(relx=0.38, rely=0.45)
lbUF.place(relx=0.38, rely=0.50)

#Definição dos campos de entrada da Tela de Agendamento
lbMatricula = tk.Entry(oJanelaAgendamento)
lbNome = tk.Entry(oJanelaAgendamento)
cbExame =ttk.Combobox(oJanelaAgendamento, values=["Admissional", "Periódico", "Retorno ao Trabalho", "Mudança de Risco", "Demissional"])
cbComplementar = ttk.Combobox(oJanelaAgendamento, values=["Sim", "Não"])
lbClinica = tk.Entry(oJanelaAgendamento)
lbCidade = tk.Entry(oJanelaAgendamento)
lbUF = tk.Entry(oJanelaAgendamento)

#Localização dos campos de entrada da Tela de Agendamento
lbMatricula.place(relx=0.47, rely=0.20, width=250, height=20)
lbNome.place(relx=0.47, rely=0.25, width=250, height=20)
cbExame.place(relx=0.47, rely=0.30, width=250, height=20)
cbComplementar.place(relx=0.47, rely=0.35, width=250, height=20)
lbClinica.place(relx=0.47, rely=0.40, width=250, height=20)
lbCidade.place(relx=0.47, rely=0.45, width=250, height=20)
lbUF.place(relx=0.47, rely=0.50, width=250, height=20)

#Define os botões da Tela de Agendamento
btInserir = tk.Button(oJanelaAgendamento, text='Inserir')
btApagar = tk.Button(oJanelaAgendamento, text='Apagar')
btSair = tk.Button(oJanelaAgendamento, text='Sair')

#localização dos botões da Tela de Agendamento
btInserir.place(relx=0.43, rely=0.80, width=100, height=30)
btApagar.place(relx=0.53, rely=0.80, width=100, height=30)
btSair.place(relx=0.63, rely=0.80, width=100, height=30)

oJanelaAgendamento.mainloop()
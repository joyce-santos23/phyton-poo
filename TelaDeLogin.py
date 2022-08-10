import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from turtle import bgcolor

#Configuração da Janela de Login
oJanelaAcesso = tk.Tk()
oJanelaAcesso.title("Login de Acesso")
oJanelaAcesso.geometry("1000x700")
oJanelaAcesso.configure(background="#C0C0C0")


#Função de validação de senha
def fValidarSenha():
    txMensagem.config(state='normal')
    if lbLogin.get() == "":
        txMensagem.delete("1.0","end")
        txMensagem.insert('É necessário inserir um login')
        if lbSenha.get == lbLogin.get:
            txMensagem.delete("1.0","end")
            txMensagem.insert('O login e a senha não podem ser iguais!')
        else:
            oJanelaAgendamento = tk.Toplevel(oJanelaAcesso)
            oJanelaAgendamento.title("Sistema de Gerenciamento de Exames")
            oJanelaAgendamento.geometry("1000x700")
            oJanelaAgendamento.configure(background="#C0C0C0")
    
    #Desabilita o campo mensagem    
    txMensagem.config(state='disabled')       


#Fonte do label Login
Titulofont = tkFont.Font(family="Lucida Grande", size=15)
Loginfont = tkFont.Font(family="Lucida Grande", size=10)
Senhafont = tkFont.Font(family="Lucida Grande", size=10)
#Definição dos campos label da tela de login
Titulo = tk.Label(oJanelaAcesso, text="SISTEMA DE GERENCIAMENTO DE EXAMES", bg="#C0C0C0", fg="#000000", font=Titulofont)
lbLogin = tk.Label(oJanelaAcesso, text="Login:", bg="#C0C0C0", fg="#000000", font=Loginfont )
lbSenha = tk.Label(oJanelaAcesso, text="Senha:", bg="#C0C0C0", fg="#000000", font=Senhafont)

#Localização dos campos label da tela de Login
Titulo.place(relx=0.3, rely=0.1)
lbLogin.place(relx=0.4, rely=0.30)
lbSenha.place(relx=0.4, rely=0.35)

#Definição dos campos de entrada da tela de login
lbLogin = tk.Entry(oJanelaAcesso)
lbSenha = tk.Entry(oJanelaAcesso)
txMensagem = tk.Text(oJanelaAcesso, state='disabled', bg="#C0C0C0")

#Localização dos campos de entrada da tela de login
lbLogin.place(relx=0.45, rely=0.30, width= 150, height=20)
lbSenha.place(relx=0.45, rely=0.35, width= 150, height=20)
txMensagem.place(relx=0.45, rely=0.38, width= 200, height=20)
#Botão de entrada Tela de login
btEntrar = tk.Button(oJanelaAcesso, text="Entrar", command=fValidarSenha)
#Localização do botão de entrada Tela de login
btEntrar.place(relx=0.48, rely=0.50, width=100, height=30)

#Define a configuração da segunda janela
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




oJanelaAcesso.mainloop()
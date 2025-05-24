import customtkinter as ctk

def dowload_area (escolha):
    if escolha == 'Fazer Download':
        textvar = ctk.StringVar(value='Abrindo áreas de Download ..')
    if escolha == 'Uploads Recentes':
        textvar = ctk.StringVar(value='Mostrando Uploads ..')
    if escolha == 'Configurações':
        textvar = ctk.StringVar(value='Sessão de Configurações ..')
    ctk.CTkLabel(janela, textvariable=textvar).pack(pady=30)

janela = ctk.CTk()
janela.title('Teste')
janela._set_appearance_mode('dark')
janela.geometry('700x400')

apresentacao = ctk.CTkLabel(janela, text='Bem-vindo ao meu App \n\n O que você procura?', font=('arial bold', 18))
apresentacao.pack()

opcoes = ctk.CTkOptionMenu(janela, values=['Fazer Download', 'Uploads Recentes', 'Configurações'], command=dowload_area)
opcoes.pack()


#Fim do Código
janela.mainloop()
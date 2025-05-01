import customtkinter as ctk 
import time

#Layout
layout = ctk.CTk() #Inicializar
layout.title('YT Video Downloader') #Título
layout._set_appearance_mode('dark') #Aparência
layout.geometry('700x400') #Tamanho padrão
layout.minsize(width=480, height=280) #tamanho mínimo
# layout.maxsize(width=1080,height=960) #Tamanho máximo
# layout.resizable(width=True, height=False) #o que é falso não dá para alterar o tamanhoo

#Textos e botões
texto1 = "Insira o texto aqui"
btn1 = ctk.CTkButton(layout, text=texto1)
btn1.pack()

#criar nova janela
def novajanela():
    new_layout = ctk.CTkToplevel(layout)
    new_layout.geometry('200x200')

btn_config = ctk.CTkButton(master=layout, text='Configurações',command=novajanela).place(x=300,y=100)
btn_view_uploads = ctk.CTkButton(master=layout, text='Visualizar Uploads', command=novajanela).place(x=1000, y=100) #Corrigir esse erro

#Fim do Código
layout.mainloop() #Manter o código funcionando 

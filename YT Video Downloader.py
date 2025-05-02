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
btn1 = ctk.CTkButton(layout, text=texto1).place(x=330, y=50)

#criar nova layout
def novajanela():
    new_layout = ctk.CTkToplevel(layout)
    new_layout.geometry('200x200')

btn_config = ctk.CTkButton(master=layout, text='Configurações',command=novajanela).place(x=15,y=100)
btn_view_uploads = ctk.CTkButton(master=layout, text='Visualizar Uploads', command=novajanela).place(x=15, y=85) #Corrigir esse erro

#Frames 
thumbnail = ctk.CTkFrame(master=layout, width=670, height=320, fg_color='#222831', bg_color='transparent', border_width=10, 
                         corner_radius=10, border_color='#948979').place(x=330, y=100)
download_options = ctk.CTkFrame(master=layout, width=380, height=600,fg_color='#393E46', bg_color='transparent').place(x=1100, y=100)
menu = ctk.CTkFrame(master=layout, width=230, height=1200, fg_color='#948979', bg_color='transparent').place(x=0,y=0)
urlbar = ctk.CTkFrame(master=layout, width=1150, height=25, bg_color='transparent').place(x=330, y=50)

#Tabview
tabview = ctk.CTkTabview(layout, width=380, height=600)
tabview.pack()
tabview.add('Pasta')
tabview.add('Renomear')
tabview.add('Qualidade do vídeo')
tabview.add('Extrair áudio')
tabview.grid(row=0, column=0, padx=1100, pady=100)

#Text
btn_360P = ctk.CTkButton(tabview.tab('Qualidade do vídeo'), text='360P')
btn_360P.grid(row=0, column=0, padx=20, pady=10)
btn_480P = ctk.CTkButton(tabview.tab('Qualidade do vídeo'), text='480P')
btn_480P.grid(row=0, column=1, padx=20, pady=10)
btn_720P = ctk.CTkButton(tabview.tab('Qualidade do vídeo'), text='720P')
btn_720P.grid(row=1, column=0, padx=20, pady=10)

#Fim do Código
layout.mainloop() #Manter o código funcionando 

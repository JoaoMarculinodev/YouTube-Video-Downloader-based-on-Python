import customtkinter as ctk 
from PIL import Image 
from pytubefix import YouTube as yt
import os 
#Funções

def insert_url ():
    global barra_de_endereco
    url = barra_de_endereco.get()
    global video
    video = yt(url)
    thumbnail_view()

def thumbnail_view():
    global video
    thumbnail_url = str(video.thumbnail_url())
    thumbnail = ctk.CTkImage(light_image=Image.open(thumbnail_url), dark_image=Image.open(thumbnail_url), size=(660, 310))
    thumb_label = ctk.CTkLabel(layout, image=thumbnail)
    thumb_label.place(x=330,y=100)

def download():
    global video
    videoquality = video.streams.get_highest_resolution()
    videoquality.download(output_path=r'C:\Users\joaom\OneDrive\Documents\Vídeos')

#Layout
layout = ctk.CTk() #Inicializar
layout.title('YT Video Downloader') #Título
layout._set_appearance_mode('dark') #Aparência
layout.geometry('700x400') #Tamanho padrão
layout.minsize(width=480, height=280) #tamanho mínimo

#Frames 
thumb_place = ctk.CTkFrame(master=layout, width=670, height=320, fg_color='#222831', bg_color='transparent', border_width=10, 
                         corner_radius=10, border_color='#948979')
thumb_place.place(x=330, y=100)
download_options = ctk.CTkFrame(master=layout, width=380, height=600,fg_color='#393E46', bg_color='transparent')
download_options.place(x=1100, y=100)
menu = ctk.CTkFrame(master=layout, width=230, height=1200, fg_color='#948979', bg_color='transparent')
menu.place(x=0,y=0)
urlbar = ctk.CTkFrame(master=layout, width=1150, height=25, bg_color='transparent')
urlbar.place(x=330, y=50)

#Entrada da URL
barra_de_endereco = ctk.CTkEntry(layout, width=1090, height=25, placeholder_text='Pesquise aqui')
barra_de_endereco.place(x=330, y=50)
buscarbtn = ctk.CTkButton(layout, text='Buscar',command=insert_url,width=15, height=25)
buscarbtn.place(x=1430,y=50)

#Tabview
tabview = ctk.CTkTabview(layout, width=380, height=600)
tabview.pack()
tabview.add('Pasta')
tabview.add('Renomear')
tabview.add('Qualidade do vídeo')
tabview.add('Extrair áudio')
tabview.grid(row=0, column=0, padx=1100, pady=100)

#Quality Choices
btn_360P = ctk.CTkButton(tabview.tab('Qualidade do vídeo'), text='360P')
btn_360P.grid(row=0, column=0, padx=20, pady=10)
btn_480P = ctk.CTkButton(tabview.tab('Qualidade do vídeo'), text='480P')
btn_480P.grid(row=0, column=1, padx=20, pady=10)
btn_720P = ctk.CTkButton(tabview.tab('Qualidade do vídeo'), text='720P')
btn_720P.grid(row=1, column=0, padx=20, pady=10)

#Download Button
downloadbtn = ctk.CTkButton(layout, command=download, width=20, height=10, text='Baixar', bg_color="transparent")
downloadbtn.place(x=330, y=430)

#Fim do Código
layout.mainloop() #Manter o código funcionando 
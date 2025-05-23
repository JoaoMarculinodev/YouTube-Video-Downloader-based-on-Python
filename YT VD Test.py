import customtkinter as ctk

janela = ctk.CTk()
janela.title('Teste')
janela._set_appearance_mode('dark')
janela.geometry('700x400')
thumbnail = ctk.CTkFrame(master=janela, width=670, height=320, fg_color='#222831', bg_color='transparent', border_width=10, 
                         corner_radius=10, border_color='#948979').place(x=330, y=100)
download_options = ctk.CTkFrame(master=janela, width=380, height=600,fg_color='#393E46', bg_color='transparent').place(x=1100, y=100)
menu = ctk.CTkFrame(master=janela, width=230, height=1200, fg_color='#948979', bg_color='transparent').place(x=0,y=0)
urlbar = ctk.CTkFrame(master=janela, width=1150, height=25, bg_color='transparent').place(x=330, y=50)

tabview = ctk.CTkTabview(janela, width=380, height=600)
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
janela.mainloop()
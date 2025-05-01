import customtkinter as ctk

janela = ctk.CTk()
janela._set_appearance_mode('dark')
janela.geometry('700x400')
thumbnail = ctk.CTkFrame(master=janela, width=670, height=320, fg_color='#222831', bg_color='transparent', border_width=10, 
                         corner_radius=10, border_color='#948979').place(x=330, y=100)
download_options = ctk.CTkFrame(master=janela, width=380, height=600,fg_color='#393E46', bg_color='transparent').place(x=1100, y=100)
menu = ctk.CTkFrame(master=janela, width=230, height=1200, fg_color='#948979', bg_color='transparent').place(x=0,y=0)
urlbar = ctk.CTkFrame(master=janela, width=1150, height=25, bg_color='transparent').place(x=330, y=50)

#Fim do Código
janela.mainloop()
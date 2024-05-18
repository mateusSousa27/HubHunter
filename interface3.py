import customtkinter
from funcoes_usadas import *


def retornar_link():
    nome_completo = entrada_nome.get()
    parametro = nome_completo.split(' ')

    cidade_formatada = entrada_localidade.get()
    cidade = cidade_formatada.replace(' ', '+')
    estado = entrada_estado.get()

    linguagem = entrada_linguagem.get()
    #print(linguagem)

    pagina_cont = 1
    total_de_paginas = 1

    while pagina_cont <= total_de_paginas:
        if(linguagem == 'none'):
            url_perfil = busca_perfil(nome_completo, cidade, estado, pagina_cont)
        else:
            url_perfil = busca_perfil_linguagem(nome_completo, cidade, estado, linguagem, pagina_cont)

        total_de_paginas = buscar_user(url_perfil, parametro[0], pagina_cont)

        pagina_cont+=1

janela = customtkinter.CTk()
janela.title("interface")
janela.geometry("1200x600")

sidebar = customtkinter.CTkFrame(master=janela, fg_color="#4B83FA", width=200, height=600, corner_radius=0)
sidebar.pack_propagate(0)
sidebar.pack(fill="y",anchor="w", side="left")

frame_principal = customtkinter.CTkFrame(master=janela, fg_color="#fff", width=1200, height=600, corner_radius=0)
frame_principal.pack_propagate(0)
frame_principal.pack(side="left")

frame_titulo = customtkinter.CTkFrame(master=frame_principal, fg_color="transparent")
frame_titulo.pack(anchor="n", fill="x",  padx=27)

titulo = customtkinter.CTkLabel(master=frame_titulo, text="Encontre o funcionario certo!", font=("Arial Black", 25), text_color="#144673")
titulo.pack(anchor="n")

nome = customtkinter.CTkLabel(master=frame_principal, text="Nome", font=("Arial Bold", 17), text_color="#177DA6")
nome.pack(anchor="nw", pady=20, padx=20)

entrada_nome =customtkinter.CTkEntry(master=frame_principal, placeholder_text="Digite o nome do candidato...", fg_color="#F0F0F0",  border_color="#177DA6", border_width=2)
entrada_nome.pack(fill="x", padx=27, ipady=10)

grid_principal = customtkinter.CTkFrame(master= frame_principal, fg_color="transparent")
grid_principal.pack( fill="x", padx=27, pady=(31,0), anchor="n")

localidade = customtkinter.CTkLabel(master=grid_principal, text="Localidade",  font=("Arial Bold", 17), text_color="#177DA6", justify="left")
localidade.grid(row=0, column=0, sticky="w")

entrada_localidade = customtkinter.CTkEntry(master=grid_principal,  placeholder_text="Cidade...", fg_color="#F0F0F0",  border_color="#177DA6", border_width=2, width=250)
entrada_localidade.grid(row=1, column=0, ipady=10)

estado = customtkinter.CTkLabel(master=grid_principal, text="Estado(sigla)",  font=("Arial Bold", 17), text_color="#177DA6", justify="left")
estado.grid(row=0, column=1, sticky="w", padx=(25,0))

entrada_estado = customtkinter.CTkEntry(master=grid_principal,  placeholder_text="Estado...", fg_color="#F0F0F0",  border_color="#177DA6", border_width=2, width=100)
entrada_estado.grid(row=1, column=1, ipady=10, padx=(24,0))

linguagem = customtkinter.CTkLabel(master=grid_principal, text="Preferência de linguagem",  font=("Arial Bold", 17), text_color="#177DA6", justify="left")
linguagem.grid(row=0, column=2, sticky="w",  padx=(25,0))

entrada_linguagem = customtkinter.CTkEntry(master=grid_principal, placeholder_text="Linguagem...", fg_color="#F0F0F0",  border_color="#177DA6", border_width=2, width=200)
entrada_linguagem.grid(row=1, column=2, ipady=10,  padx=(21,0))

pesquisar = customtkinter.CTkButton(master=grid_principal, text="pesquisar",  width=150, fg_color="#177DA6", font=("Arial Bold", 17), border_color="#177DA6", hover_color="#45A9BF", border_width=2, text_color="#fff", command=retornar_link)
pesquisar.grid(row=1, column=3,  ipady=10, padx=(20))

frame_caixa_texto = customtkinter.CTkFrame(master=frame_principal,fg_color="transparent", width=1200)
frame_caixa_texto.pack(fill="both",  anchor="n", padx=1)

caixa_de_texto = customtkinter.CTkTextbox(master=frame_caixa_texto,fg_color="#F0F0F0", width=600, corner_radius=8)
caixa_de_texto.pack(fill = "both", padx=27, pady=20)

janela.mainloop()
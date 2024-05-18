import requests
from bs4 import BeautifulSoup

#estruturar url caso a linguagem seja informada
def busca_perfil_linguagem(usuario, cidade, estado, linguagem, pagina_cont):
      usuario_url = usuario.replace(" ", "+")

      if(linguagem == 'c++'):
           linguagem = 'C%2B%2B'

      base_url = 'https://github.com/search?q={usuario_url}+location%3A{cidade}%2C{estado}++language%3A{linguagem}&type=users&p={pagina_cont}'

      return base_url.format(usuario_url=usuario_url, cidade=cidade, estado=estado, linguagem=linguagem, pagina_cont=pagina_cont)

#estruturar a url sem linguagem
def busca_perfil(usuario, cidade, estado,pagina_cont):
      usuario_url = usuario.replace(" ", "+")

      base_url = 'https://github.com/search?q={usuario_url}+location%3A{cidade}%2C{estado}&type=users&p={pagina_cont}'

      return base_url.format(usuario_url=usuario_url, cidade=cidade, estado=estado, pagina_cont=pagina_cont)

#buscar e retornar informações 
def buscar_user(url, texto_procurado, pagina_cont):

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print("Erro ao acessar a pagina: ", e)
        
        contador = 0
        tamanho_lista = 10
        conteudo = response.text

        #verificando se o nome de usuario esta presente nas informações
        if texto_procurado in conteudo:      
            pesquisador = conteudo

            #criando medidas de buscas
            fragmentacao = conteudo.split('"display_login":')

            paginas_encontradas = pesquisador.find('"page_count":')
            fim_paginas_encontradas = pesquisador.find(',"elapsed_millis"')

            encontrar = pesquisador.find('"result_count":')
            encontrar_fim = pesquisador.find(',"facets":')

            total_de_users = pesquisador[encontrar+15:encontrar_fim]

            total_de_paginas_encontradas = int(pesquisador[paginas_encontradas+13:fim_paginas_encontradas])

        
        #conferindo o total de usuario e ajustando a pesquisa
        if(pagina_cont <= int(total_de_users[0])):
         tamanho_lista = 10
        else:
         tamanho_lista = int(total_de_users[1])

        if(int(total_de_users)<10):
             tamanho_lista = total_de_users

        if(int(total_de_users) > 0):    

            #retornando o link de todos os usuarios listados 
            while contador < int(tamanho_lista):

                        texto = "".join(fragmentacao[contador])

                        finder = texto.find('"login":"') + 9

                        print("https://github.com/"+texto[finder:-2])

                        contador +=1

            
        else:
            print('Nome não encontrado na página.')
            
        return total_de_paginas_encontradas

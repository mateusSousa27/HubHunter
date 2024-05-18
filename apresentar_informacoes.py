import funcoes_usadas

nome_completo = 'Mateus'
parametro = nome_completo.split(' ')
parametro = parametro[0].lower()

cidade = 'Fortaleza'
estado = 'ce'
linguagem = 'none'

teste_cont = 0

pagina_cont = 1
total_de_paginas = 1


while pagina_cont <= total_de_paginas:
    if(linguagem == 'none'):
        url_perfil = funcoes_usadas.busca_perfil(nome_completo, cidade, estado, pagina_cont)
    else:
        url_perfil = funcoes_usadas.busca_perfil_linguagem(nome_completo, cidade, estado, linguagem, pagina_cont)

    total_de_paginas = funcoes_usadas.buscar_user(url_perfil, parametro[0], pagina_cont)

    pagina_cont+=1

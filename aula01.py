# primeiro programa - web semantica - Rodrigo M Zanco - 205541

import requests
import re
import pprint

url = "https://www.dac.unicamp.br/sistemas/catalogos/grad/catalogo2019/cursos.html"

try:
    resp = requests.get(url)

    print('Status: ', resp.status_code)
    print('Encoding: ', resp.encoding)

    status = resp.status_code
    codificacao = resp.encoding
    conteudo = resp.content

    print('Bytes: ', len(conteudo))

    conteudo_str = conteudo.decode(codificacao)

    conteudo_list = conteudo_str.splitlines()

    cod = input("Digite o código do Curso: ")

    for l in conteudo_list:

        indice = len(conteudo_list) - 1
        ultimo = conteudo_list[indice]
        str_cod = str(cod)

        result = re.search(r"\b" + str_cod + r"\b", l)

        # print(..., l[46/44/42:-9].(...)) <- filtrar para apenas ser o nome do curso.
        
        if result is not None:
            if len(cod) == 3:
                print("Founded course: ", l[46:-9].encode(codificacao).decode('utf-8'))
                break
            elif len(cod) == 2:
                print("Founded course: ", l[44:-9].encode(codificacao).decode('utf-8'))
                break
            else:
                print("Founded course: ", l[42:-9].encode(codificacao).decode('utf-8'))
                break

        if l == ultimo:
            if result is None:
                print("Course not found.")

    # PPrint
    # pprint.pprint(conteudo.decode(resp.encoding))

except:
    print('Don\'t working', url)

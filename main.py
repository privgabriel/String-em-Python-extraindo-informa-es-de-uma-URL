url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
indice_interrogacao = url.find('?')
parametro_busca = "moedaOrigem"

url_parametros = url[indice_interrogacao+1:]
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find("&", indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(url_parametros)
print(indice_parametro)
print(valor)
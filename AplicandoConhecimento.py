from collections import defaultdict

def map_func(dados):
    result = []
    for frase in dados:
        for palavra in frase.split():
            palavra_limpa = palavra.strip(",.()\"").lower()
            result.append((palavra_limpa, 1))
    return result

def reduce_func(mapped_data):
    resultado = defaultdict(int)
    for palavra, contagem in mapped_data:
        resultado[palavra] += contagem
    return resultado

def top_palavras(reduced_data, n=10):
    return sorted(reduced_data.items(), key=lambda x: x[1], reverse=True)[:n]

with open("arquivo_mapreduce.txt", "r", encoding="utf-8") as arquivo:
    dados = arquivo.readlines()

mapped_data = map_func(dados)

reduced_data = reduce_func(mapped_data)

top_10 = top_palavras(reduced_data)

print("Top 10 palavras com maior número de ocorrência:")
for palavra, contagem in top_10:
    print(f"{palavra}: {contagem}")
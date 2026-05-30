import random

#lista com autores disponiveis para geração aleatoria 
autores = ['Tolkien', 'Shakespeare', 'Dostoiévski', 'Wilde', 'Tolstói']

#cria cada livro com titulo sequencial e dados aleatorios 
acervo = []
for i in range(1, 51):
    livro = {
        'titulo': f'Livro {i:02d}',
        'autor': random.choice(autores),
        'ano': random.randint(1800, 2023)
    }
    acervo.append(livro)
print(' ==================== LISTA GERADA =====================  ')
#Exibe os 3 primeiros livros gerados 
for livro in acervo[:3]:
    print(f"Título: {livro['titulo']} | Autor: {livro['autor']:<15} |  Ano: {livro['ano']}")

def insertion_sort(lista, chave):
    #ordena a lista de livros pela chave informada
    #percorre a lista da esquerda para a direita
    #a cada passo insere o elemento na posição correta 
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i -1
        while j >=0 and lista[j][chave] > atual[chave]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual 
    return lista 
print(' ================ ORDENAÇÃO POR TITULO ================ ')
#chama o insertion_sort e exibe os 3 primeiros livros ordenados
insertion_sort(acervo,  'titulo')
for livro in acervo[:3]:
    print(f"Título: {livro['titulo']} | Autor: {livro['autor']:<15} | Ano: {livro['ano']}")



def busca_linear(lista, titulo):
    #percorre a lista ivro por livro contando comparações 
    comparacoes = 0
    for livro in lista:
        comparacoes += 1 
        if livro['titulo'] == titulo:
            return livro, comparacoes 
    return None, comparacoes 


def busca_binaria(lista, titulo):
    #busca binaria na lista ordenada contando comparações 
    esquerda = 0
    direita = len(lista) - 1
    comparacoes = 0
    while esquerda <= direita:
        comparacoes += 1
        meio = (esquerda + direita) // 2
        if lista[meio]['titulo'] == titulo:
            return lista[meio], comparacoes
        elif lista[meio]['titulo'] <titulo:
            esquerda = meio + 1
        else:
            direita = meio -1
    return None, comparacoes 
print(' =============== BUSCA LINEAR vs BINÁRIA =============== ')
#chama a busca linear e binária e exibe as comparações
resultado, comp = busca_linear(acervo, 'Livro 25')
print('Linear - comparações:', comp)

resultado, comp = busca_binaria(acervo, 'Livro 25')
print('Binária - comparações:', comp)


def busca_por_intervalo(lista, ano_inicio, ano_fim):
    #retorna todos os livros publicados entre os dois anos informados 
    resultado = []  
    for livro in lista:
        if livro['ano'] >= ano_inicio and livro['ano'] <= ano_fim:
            resultado.append(livro)
    return resultado 
print(' =========== BUSCA POR INTERVALO (1900-1950) ============ ')
#chama a busca por intervalo e exibe os livros encontrados
resultado = busca_por_intervalo(acervo, 1900, 1950)
for livro in resultado:
    print(livro['titulo'], '-' , livro['ano'])



def benchmark(lista):
    #executa as duas buscas para 5 titulos e exibe tabela comparativa 
    titulos = ['Livro 01', 'Livro 12', 'Livro 25', 'Livro 35', 'Livro 49']
    print(f"{'(titulo)':<20} | {'(linear)':^16} | {'(binaria)':^16}")
    print('_' * 58)
    for titulo in titulos:
        _, comp_linear = busca_linear(lista, titulo)
        _, comp_binaria = busca_binaria(lista, titulo)
        print(f"{titulo:<20} | {comp_linear:^16} | {comp_binaria:^16}")
    print('_' * 58)
print(' ======================= BENCHMARK ======================= ')
#chama o benchmark e exibe a tabela comparativa
benchmark (acervo)



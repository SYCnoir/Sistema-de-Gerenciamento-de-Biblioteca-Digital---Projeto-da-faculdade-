
#==========essa lista guarda as informações e dados de os todos livros da biblioteca===========
catalogo = [
    {
        'titulo': 'Hobbit',
        'autor': 'J.R.R Tolkien',
        'ano': 1937,
        'isbn': '978-85-359-0277-1',
        'disponivel': True
    },
    {
       'titulo': 'O Morro Dos Ventos Uivantes',
       'autor': 'Emily Brontë',
       'ano': 1847,
       'isbn': '978-85-943-1823-7',
       'disponivel': True
    },
    {
     'titulo': 'Noites Brancas',
     'autor': 'Fiódor Dostoiévski',
     'ano': 1848,
     'isbn': '978-65-509-7028-4',
     'disponivel': False
    },
    {
        'titulo': 'O Retrato De Dorian Gray',
        'autor': 'Oscar Wilde',
        'ano': 1890,
        'isbn':'978-65-509-7029-1',
        'disponivel': True
    },
    {
        'titulo': 'Entendendo Algoritmos',
        'autor': 'Aditya Y. Bhargava',
        'ano': 2016,
        'isbn':'978-85-7522-563-9',
        'disponivel': False
    },
    {
        'titulo': 'Sussurro',
        'autor': 'Becca fitzapatrick',
        'ano': 2009,
        'isbn':'978-85-98078-78-6',
        'disponivel': True
    },
    {
        'titulo': 'A morte De Ivan Ilitch',
        'autor': 'Liev Tolstói',
        'ano': 1886,
        'isbn':'978-65-555-2894-7',
        'disponivel': True
    },
    {
        'titulo': 'Hamlet',
        'autor': 'william Shakespeare',
        'ano': 1602,
        'isbn':'978-65-555-2206-8',
        'disponivel': True
    },
    {
        'titulo': 'O Pequeno Principe',
        'autor': 'Antoine de Saint-exupéry',
        'ano': 1943,
        'isbn':'978-65-5552-136-8',
        'disponivel': False
    },
    {
        'titulo': 'O Livro Dos Cinco Anéis',
        'autor': 'miyamoto musashi',
        'ano': 1645,
        'isbn':'978-65-85168-34-2',
        'disponivel': True
    }

]

def busca_linear(catalogo,titulo):
    # busca um livro pelo título na lista
    # percorre livro por livro contando as comparações
    # retorna o livro se encontrar, ou None se não encontrar
    comparacoes = 0 
    for livro in catalogo:
        comparacoes = comparacoes + 1
        if livro['titulo'].lower() == titulo.lower():
            print('comparações:', comparacoes)
            return livro, comparacoes 
    return None, 0
print(" ========== BUSCA LINEAR ========== ")  

# chama a função busca_linear e guarda o resultado
resultado, comp_linear = busca_linear(catalogo, 'Sussurro')

# verifica se algum livro foi encontrado
if resultado  != None:
    # Exibe os dados do livro encontrado 
    print('Livro encontrado!')
    print('Título:', resultado['titulo'])
    print('Autor:', resultado['autor'])
    print('Ano:', resultado['ano'] )
else:
    # caso o titulo não exita dentro do catalogo exibe uma mensagem
    print('livro não encontrado no catálogo!')

# ordena o catalogo em ordem alfabética pelo título
catalogo_ordenado = sorted(catalogo, key=lambda livro: livro['titulo'] )

def busca_binaria(catalogo_ordenado,titulo):
    #vai marcar o inicio e o fim da lista
    #depois vai contar quantas comparações foram feitas
    #vai repetit enquanto ainda tiver livros para verificar e calcular a posição do livro do meio
    #se encontrar o livro, vai retornar os dados 
    #se o meio vem antes ele busca alfabeticamente, na metade direta
    #se o meio vem depois, ele busca na metade da esquerda, caso nao ache Retorna None
    esquerda = 0
    direita = len(catalogo_ordenado) - 1 
    comparacoes = 0 
    while esquerda <= direita:
        comparacoes = comparacoes + 1 
        meio = (esquerda + direita) // 2
        titulo_meio = catalogo_ordenado[meio]['titulo'].lower()
        if titulo_meio == titulo.lower():
            print('comparações:', comparacoes)
            return catalogo_ordenado[meio], comparacoes 
        elif titulo_meio < titulo.lower():
            esquerda = meio + 1 
        else:
            direita = meio - 1 
    return None, 0
print(" ========== BUSCA BINARIA  ========== ")

#chama função de busca binaria
resultado, comp_binaria = busca_binaria(catalogo_ordenado,  'Hamlet')
#verifica se foi encontrado e apresenta os dados
if resultado !=None:
    print('Livro encontrado!')  
    print('Título:', resultado['titulo'])
    print('Autor:', resultado['autor'])
    print('Ano:', resultado['ano'])
#caso o livro nao exista, é mostrado essa mensagem
else: 
    print('Livro não encontrado!')
#Filta os livros do catalogo por qualqiuer campo e valor informado
#depois retorna uma nova lista com apenas os livros que correspondem ao filtro

print('Busca linear:', comp_linear, 'comparações')
print('Busca binária:', comp_binaria, 'comparações')
print('A busca binária foi mais eficiente')
#comparação q prof pediu


def filtrar(catalogo, campo, valor):
    resultado = []
    for livro in catalogo:
        if livro[campo]== valor: 
            resultado.append(livro)
    return resultado 
print(" ========== LIVROS DISPONIVEIS ========== ")
livros_disponiveis = filtrar(catalogo, 'disponivel', True)
for livro in livros_disponiveis:
    print(livro['titulo'])

#calcula we retorna informações gerais do catálogo
def estatisticas(catalogo):
    total = len(catalogo)
    disponiveis = 0
    emprestados = 0
 #conta o total de livros disponiveis ou emprestados
    for livro in catalogo:
        if livro['disponivel'] == True:
            disponiveis = disponiveis + 1 
        else:
            emprestados = emprestados + 1 
 #encontra o livro mais antigo sem usar min() ou max()  
    mais_antigo = catalogo[0]
    for livro in catalogo:
        if livro['ano'] < mais_antigo['ano']:
            mais_antigo = livro 
    return total, disponiveis, emprestados, mais_antigo 
print(" ========== ESTATISTICAS  ========== ")   
#apresenta os dados 
total, disponiveis, emprestados, mais_antigo = estatisticas(catalogo)
print('Total:',total)
print('Disponiveis:', disponiveis)
print('Emprestados:', emprestados)
print('Livro mais antigo:', mais_antigo['titulo'],  '-', mais_antigo['ano'])

from dataclasses import dataclass, field
import copy 

#dataclass Leitor define a estrutura de dados do leitor
@dataclass
class Leitor:
    nome: str      #nome completo do leitor
    matricula: str #codigo de identificação
    email: str     #email do leitor
    emprestimos_ativos: list = field(default_factory=list)   #livros ja emprestados
    historico: list = field(default_factory=list)            #livros devolvidos 

    def total_ativos(self):
        #retorna a quantidade de emprestimos ativos
        return len(self.emprestimos_ativos)
    
    def pode_emprestar(self):
        #verifica se o leitor pode mpegar mais livros (limite 3)
        return len(self.emprestimos_ativos) < 3

#dataclass Livro define a estrutura de dados do livro
@dataclass
class Livro:
    titulo: str             #titulo do livro
    autor: str              #autor do livro
    ano: int                #ano de publicação
    isbn: str               #codigo unico do livro
    disponivel: bool = True #disponibilidade do livro

    def __str__(self):
         #retorna uma linha formatada com os dados do livro 
         return f"{self.titulo} - {self.autor} ({self.ano}) | Disponivel: {self.disponivel}"

#lista com os leitores da biblioteca
leitores = [
    Leitor('Amanda Silva', 'MAT001', 'amanda@gmail.com'),
    Leitor('Bruno Costa', 'MAT002', 'bruno@gmail.com'),
    Leitor('Carla Souza', 'MAT003', 'carla@gmail.com'),
    Leitor('Diego Lima', 'MAT004', 'diego@gmail.com'),
    Leitor('Elena Santos', 'MAT005', 'elena@gmail.com'),
]

#lista com os livros da biblioteca
livros = [
    Livro('Hobbit', 'J.R.R Tolkien', 1937, '978-85-359-0277-1'),
    Livro('Hamlet', 'William Shakespeare', 1602, '978-65-555-2206-8'),
    Livro('Sussurro', 'Becca Fitzpatrick', 2009, '978-85-98078-78-6'),
    Livro('Noites Brancas', 'Fiódor Dostoiévski', 1848, '978-65-509-7028-4'),
    Livro('O Pequeno Principe', 'Antoine de Saint-Exupéry', 1943, '978-65-5552-136-8'),
    Livro('O Retrato De Dorian Gray', 'Oscar Wilde', 1890, '978-65-509-7029-1'),
    Livro('A Morte De Ivan Ilitch', 'Liev Tolstói', 1886, '978-65-555-2894-7'),
    Livro('O Morro Dos Ventos Uivantes', 'Emily Brontë', 1847, '978-85-943-1823-7'),
    Livro('O Livro Dos Cinco Anéis', 'Miyamoto Musashi', 1645, '978-65-85168-34-2'),
    Livro('Entendendo Algoritmos', 'Aditya Y. Bhargava', 2016, '978-85-7522-563-9'),
]

#matriz de emprestimos: 6 leitores x 7 dias 
matriz = [
    [2, 0, 1, 3, 0, 1, 0],  # Amanda
    [0, 1, 0, 2, 1, 0, 2],  # Bruno
    [1, 1, 2, 0, 1, 0, 0],  # Carla
    [0, 0, 1, 1, 0, 2, 1],  # Diego
    [3, 1, 0, 0, 2, 1, 0],  # Elena
    [1, 2, 1, 0, 0, 0, 3],  # Fábio
]

dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']

def emprestar(leitor, livro):
    #verifica se o livro esta disponivel e se o leitor pode pegar mais livros
    if livro.disponivel == False:
        print('Livro indisponivel!')
        return False 
    if leitor.pode_emprestar() == False:
        print('Leitor atingiu o limite de 3 empréstimos!')
        return False 
    livro.disponivel = False 
    leitor.emprestimos_ativos.append(livro.titulo)
    print(f'Empréstimo realizado! {livro.titulo} > {leitor.nome}')
    return True 

def devolver(leitor, livro):
    #remove o livro dos ativos, adiciona ao historico e marca como disponivel 
    leitor.emprestimos_ativos.remove(livro.titulo)
    leitor.historico.append(livro.titulo)
    livro.disponivel = True 
    print(f'{livro.titulo} devolvido por {leitor.nome}')
    return True

def backup_acervo(livros):
    #retorna uma copia profunda e segura  do acervo
    return copy.deepcopy(livros)

def busca_linear(livros, titulo):
    #percorre a lista livro por livro contando comparações 
    comparacoes = 0
    for livro in livros:
        comparacoes += 1 
        if livro.titulo.lower() == titulo.lower():
            return livro, comparacoes 
    return None, comparacoes 

def filtrar(livros, campo, valor):
    #filtrar os livros por qualquer campo e valor informado 
    resultado = []
    for livro in livros:
        if getattr(livro, campo) == valor:
            resultado.append(livro)
    return resultado 

def relatorio_final(livros, leitores, matriz, dias):
    #gera o relatorio completo da biblioteca
    total = len(livros)
    disponiveis = 0 
    emprestados = 0
    for livro in livros:
        if livro.disponivel:
            disponiveis += 1
        else:
            emprestados += 1 
    
    #encontra o leitor mais ativo 
    mais_ativo = leitores[0]
    for leitor in leitores:
        if leitor.total_ativos() > mais_ativo.total_ativos():
            mais_ativo = leitor
    
    #encontra o dia com mais retirada 
    totais_dias = []
    for coluna in range(7):
        total_dia = 0
        for linha in matriz:
            total_dia += linha[coluna]
        totais_dias.append(total_dia)
    
    maior = 0 
    indice_dia = 0
    for i in range(len(totais_dias)):
        if totais_dias [i] > maior: 
            maior = totais_dias[i]
            indice_dia = i

    print('╔══════════════════════════════════════════╗')
    print('║     RELATÓRIO FINAL — BIBLIOTECA DIGITAL ║')
    print('╠══════════════════════════════════════════╣')
    print(f'║ Total de livros:       {total:<18}║')
    print(f'║ Livros disponíveis:    {disponiveis:<18}║')
    print(f'║ Livros emprestados:    {emprestados:<18}║')
    print('╠══════════════════════════════════════════╣')
    print(f'║ Leitor mais ativo:     {mais_ativo.nome:<18}║')
    print(f'║ Dia com mais retiradas: {dias[indice_dia]:<18}║')
    print('╚══════════════════════════════════════════╝')

#simula 10 operações mistas
def simular_operacoes():
        #salva backup antes das operações
        bkp = backup_acervo(livros)
        print('Backup salvo!')

        #4 emprestimos
        emprestar(leitores[0], livros[0])
        emprestar(leitores[0], livros[1])
        emprestar(leitores[1], livros[2])
        emprestar(leitores[2], livros[3])

        #2 devoluções 
        devolver(leitores[0], livros[0])
        devolver(leitores[1], livros[2])
        
        #2 buscas
        resultado, comp = busca_linear(livros, 'Hamlet')
        print(f'Busca: Hamlet encontrado em {comp} comparações')
        resultado, comp = busca_linear(livros, 'Sussurro')
        print(f'Busca: Sussurro encontrado em {comp} comparações')

        #2 filtros
        disponiveis = filtrar(livros, 'disponivel', True)
        print(f'Livros disponíveis: {len(disponiveis)}')
        tolkien = filtrar(livros, 'autor', 'J.R.R Tolkien')
        print(f'Livros de Tolkien: {len(tolkien)}')
    
def menu():
    #menu da navegação da biblioteca 
    while True:
        print('\n=== MENU ===')
        print('[1] Buscar livro')
        print('[2] Emprestar')
        print('[3] Devolver')
        print('[4] Relatório')
        print('[0] Sair')
        opcao = input('Escolha: ')
        if opcao == '1':
            titulo = input('Digite o titulo: ')
            resultado, comp = busca_linear(livros, titulo)
            if resultado:
                print(resultado)
            else:
                print('Livro não encontrado!')
        elif opcao == '2':
            nome = input('Nome do leitor: ')
            titulo = input('Titulo do livro: ')
            leitor = next((l for l in leitores if l.nome.lower()  == nome.lower()), None)
            livro = next((l for l in livros if l.titulo.lower()  == titulo.lower()), None)
            if leitor and livro:    
                emprestar(leitor, livro)
            else:
                print('Leitor ou livro não encontrado!')
        elif opcao == '3':
            nome = input('Nome do leitor: ')
            titulo = input('Titulo do livro: ')
            leitor = next((l for l in leitores if l.nome.lower() == nome.lower()), None)
            livro = next((l for l in livros if l.titulo.lower() == titulo.lower()), None)
            if leitor and livro:
                devolver(leitor, livro)
            else:
                print('Leitor ou livro não encontrado!')
        elif opcao == '4':
            relatorio_final(livros, leitores, matriz, dias)
        elif opcao == '0':
            print('Saindo...')
            break


#executa as operações e abre o menu 
simular_operacoes()
relatorio_final(livros, leitores, matriz, dias)
menu()


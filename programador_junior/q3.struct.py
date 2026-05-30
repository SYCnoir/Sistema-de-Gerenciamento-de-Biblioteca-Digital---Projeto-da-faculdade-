from dataclasses import dataclass, field 
#define a estrutura de dados do leitor com seus ncampos e metódos 
@dataclass 
class Leitor:
    nome: str                           #nome completo do leitor
    matricula: str                      #codigo de identificação do leitor  
    email: str                          #email do leitor
    emprestimos_ativos: list = field(default_factory=list)   #livros atualmente emprestados
    historico: list = field(default_factory=list)            #livros ja devolvidos 
    def total_ativos(self):
        #retorna a quantidade de emprestimos ativos do leitor 
        return len(self.emprestimos_ativos)
  
    def total_historico(self):
        #retorna a quantidaede atual de livros ja emprestados
        return len(self.historico)

    def pode_emprestar(self):
        #verifica se o leitor pode pegar mais livros (limite de 3 ativos)
        return len(self.emprestimos_ativos) < 3 


#define  a estrutura de dados do livro com seus campos e metodos de exibição
@dataclass 
class Livro:
     titulo: str     #titulo livro
     autor: str      #autor do livro
     ano: int        #ano de publicao
     isbn: str       #codigo do livro
     disponivel:bool = True

     def __str__(self):
       #retorna uma linha formatada com os dados do livro 
       return f"{self.titulo} - {self.autor} ({self.ano}) | Disponivel: { self.disponivel}"
     
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
    Livro('O morro dos ventos uivantes','Emily Brontë', 1847, '978-85-943-1823-7'),
    Livro('Noites Brancas', 'Fiódor Dostoiévski', 1848, '978-65-509-7028-4'),
    Livro('O Retrato De Dorian Gray','Oscar Wilde', 1890, '978-65-509-7029-1'),
    Livro('Entendendo Algoritmos','Aditya Y. Bhargava', 2016, '978-85-7522-563-9'),
    Livro('Sussurro','Becca fitzapatrick', 2009, '978-85-98078-78-6'),
    Livro('A morte De Ivan Ilitch','Liev Tolstói', 1886, '978-65-555-2894-7'),
    Livro('Hamlet','william Shakespeare', 1602, '978-65-555-2206-8'),
    Livro('O Pequeno Principe','Antoine de Saint-exupéry', 1943, '978-65-5552-136-8'),
    Livro('O Livro Dos Cinco Anéis','miyamoto musashi', 1645, '978-65-85168-34-2'),
]
def emprestar (leitor, livro):
         #verifica se o livro esta disponivel
         if livro.disponivel == False:
             print('Livro indisponivel!')
             return False 
         #VERIfica se pode pegar mais livros
         if leitor.pode_emprestar() == False:
             print('Leitor atingiu o limite de 3 empréstimos!')
             return False
         #realiza emprestimo
         livro.disponivel = False
         leitor.emprestimos_ativos.append(livro.titulo)
         print(f'empréstimo realizado! {livro.titulo} emprestado para {leitor.nome}')
         return True 
#testa o emprestyimo e mostra os livros ativos do leitor
print(' ============================ EMPRÉSTIMO ============================ ')
emprestar(leitores[2], livros[8])
print(leitores[2].emprestimos_ativos)
 
def devolver(leitor, livro):
   #remove o livro dos emprestimos ativos
   leitor.emprestimos_ativos.remove(livro.titulo)
   #adiciona no historico do leitor
   leitor.historico.append(livro.titulo)
   #marca o livro como disponivel novamente 
   livro.disponivel = True 
   print(f'{livro.titulo} devolvido por {leitor.nome}')
   return True
#testa devolução      
print(' ============================= DEVOLUÇÃO ============================ ')
devolver(leitores[2], livros[8])
print(leitores[2].historico)
print(' ======================== RELATÓRIO DO LEITOR ======================= ')
def relatorio_leitor(leitor):
   #exibe  o relatorio completo da ficha do leitor
   print(' ___________________________ ficha leitor ___________________________')
   print('                         Nome:', leitor.nome)
   print('                         Matricula:', leitor.matricula)
   print('                         Email:', leitor.email)
   print('                         Emprestimos ativos:', leitor.emprestimos_ativos)
   print('                         Total ativos:', leitor.total_ativos())
   print('                         Histórico:', leitor.historico)
   print('                         Total históricos:', leitor.total_historico())
   print('                         Pode emprestar:', leitor.pode_emprestar())

#testa o relatorio completo da ficha do leitor       
relatorio_leitor(leitores[2])

    
 
    

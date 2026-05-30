import copy


#lista com 5 livros para demonstração 
acervo = [
    {'titulo': 'Hobbit', 'disponivel': True},
    {'titulo': 'Hamlet', 'disponivel': True},
    {'titulo': 'Sussurro', 'disponivel': True},
    {'titulo': 'Noites Brancas', 'disponivel': True},
    {'titulo': 'O Pequeno Principe', 'disponivel': True},
]
#demonstra o problema da atribuição direta 
print('============= DEMONSTRAÇÃO: ATRIBUIÇÃO DIRETA =============')
copia = acervo 
print('Original antes:', acervo[0])
copia[0]['disponivel'] = False 
print('Original depois:', acervo [0])
print('PROBLEMA: o original foi alterado!')

#DEmonstra o problema com copy.copy()
print('================ DEMONSTRAÇÃO: COPY.COPY() ================')
acervo[0]['disponivel'] = True  #reseta o original ai
copia_rasa = copy.copy(acervo)
print('Original antes:', acervo[0])
copia_rasa[0]['disponivel'] = False
print('Original depois:', acervo[0])
print('PROBLEMA: os dicts internos ainda são compartilhados!')

#demonstra a solução com copy.deepcopy()
print('================ SOLUÇÃO: COPY.DEEP.COPY() ================')
acervo[0]['disponivel'] = True  #reseta o orginal
copia_profunda = copy.deepcopy(acervo)
print('Original antes:', acervo[0])
copia_profunda[0]['disponivel'] = False 
print('Original depois:', acervo[0])   
print('OK: o original está protegido!')


def backup_acervo(acervo):
    #retorna uma copia profunda e segura do acervo
    return copy.deepcopy(acervo)

#testa o backup  
backup = backup_acervo(acervo)
backup[1]['disponivel'] = False
print('====================== BACKUP_ACERVO ======================')
print('Original:', acervo[1])
print('Backup:', backup[1])
print('OK: original protegido!') 


def comparar_referencias(obj_a, obj_b):
    #verifica se dois objetos apontam para o mesmo lugar na memoria 
    print('=================== COMPARAR REFERENCIAS ===================')
    print('ID obj_a:', id(obj_a))
    print('ID obj_b:', id(obj_b))
    if obj_a is obj_b:
        print('MESMA referência! os dois nomes apontam para o mesmo objeto na memoria.')
        print('Modificar um VAI alterar o outro')
    else:
        print('Referências DIFERENTES! são objetos independentes na memoria.')
        print('Modificar um não vai alterar o outro')

#testa com atribuição direta 
copia_direta = acervo 
comparar_referencias(acervo, copia_direta)

#testa com deepcopy 
copia_segura = copy.deepcopy(acervo)
comparar_referencias(acervo, copia_segura)

 
  #!!!!!!!!!!!!!!!ORGANIZAR E CONFIRMAR SE OS COMENTARIOS ESTAO CERTOS AMANHÃ!!!!!!!!!!!!!!!!!!!!!!!!!!

#NOME DOS LEITORES
leitores = ['amanda','bruno','carla','diego','elena','fabio']

#dias da semana
dias = ['seg','ter','qua','qui','sex','sab','dom']

#matriz de empréstimos : cada linha é um leitor, cada coluna é um dia
matriz = [
    [2,0,1,3,0,1,0], #amanda
    [0,1,0,2,1,0,2], #bruno
    [1,1,2,0,1,0,0], #carla
    [0,0,1,1,0,2,1], #diego
    [3,1,0,0,2,1,0], #elena
    [1,2,1,0,0,0,3], #fabio

]
def total_por_leitor(matriz):
    #percorre cada leitor da linha da matriz
    #soma os emprestimos de cada linha do leitor 
    #e dps retorna uma lista com o total de cada leitor
    totais = []
    for linha in matriz:
        total = 0
        for numero in linha:
            total = total + numero 
        totais.append(total)
    return totais 
print('======================= TOTAL POR LEITOR =======================')
print(total_por_leitor(matriz))

#________________________________________________________________________________________
def total_por_dia(matriz):
    #passa por cada coluna de cada da matriz
    #soma os emprestimos dos leitores naquele dia
    #retorna uma lista com o total do emprestimo de cada dia 
    totais = []
    for coluna in range(7):
        total = 0
        for linha in matriz:
            total = total + linha[coluna]
        totais.append(total)
    return totais
print('======================== TOTAL POR DIA =========================')

print(total_por_dia(matriz))

#___________________________________________________________________________________

def dia_mais_movimentado(matriz):
    #encontra o indice do dia com mais emprestimo
    #Anda nos totais diarios comparando cada valor
    #e retorna o indice do dia mais movimentado sem usar o max()
    totais = total_por_dia(matriz)
    maior = 0
    indice = 0 
    for i in range(len(totais)):
     if totais [i] > maior: 
         maior = totais[i]
         indice = i 
    return indice

print('====================== DIA MAIS MOVIMENTADO ====================')
indice = dia_mais_movimentado(matriz)
print('dia mais movimentado:',  dias[indice])

#______________________________________________________________________________
def transposta(matriz):
    #cria uma nova matriz invertendo linhas e colunas 
    #linhas viram colunas e colunas viras linhas
    #retorna a matriz transposta 7x6
    resultado = [[0]*6 for _ in range(7)]
    for i in range(6):
        for j in range(7):
            resultado[j][i] = matriz[i][j]
    return resultado 

print('========================== TRANSPOSTA ==========================')

resultado = transposta(matriz)
for i in range(7):
    print(f"{dias[i]:7}", end='')
    for valor in resultado[i]:
        print(f"{valor:6}", end='')
    print()
#_______________________________________________________________________________

print('==================== TABELA DE EMPRÉSTIMOS =====================')
#exibe a matriz formatada como tabela com cabeçalho e totais
print(f"{'':11}", end='')
for dia in dias:
    print(f"{dia:5}", end='')
print('|   total')
totais_leitor = total_por_leitor(matriz)
#imprime cada leitor com seus emprestimos e total
for i in range(6):
    print(f"{leitores[i]:8}", end='')
    for j in range(7):
        print(f"{matriz[i][j]:5}", end='')
    print(f"   |{totais_leitor[i]:6}")
#linha separada e total por dia
print('-' * 55)
totais_dias = total_por_dia(matriz)
print(f"{'total':8}", end='')
for total in totais_dias:
    print(f"{total:5}", end='')
print()

    












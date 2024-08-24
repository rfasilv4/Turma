#Menu:

#	1 - Adicionar novo Aluno | Nota (limite 10 alunos)
#    2 - Editar Aluno | Nota
#    3 - Listar os Alunos
#    4 - Excluir um Aluno
#    5 - Calcular a média da turma
#    6 - Consultar um aluno
#    7 - Apagar todos os alunos da sala

#Escolha:

#* Limite máximo de 10 alunos
#* Não pode adicionar alunos com nomes repetidos
#* Não pode aceitar notas inválidas
#       0.0 - 10.0
#	   Verificar se é número

import os
os.system("cls")
turma = {}

def adicionar(turma : dict):
   count =0
   while count <2:
        try:
         nome = input("Digite o nome do aluno: ")
         if not nome.isalpha():
            print("O nome deve ser alfabetico!")
            continue
         elif  nome in turma:
            print("Aluno já existe!")
            continue

         nota = float(input("Digite a nota: "))
         if nota < 0:
            print("Nota invalida, só aceitamos valores entre 0 e 10")
        
         elif nota > 10:
            print("Nota invalida, só aceitamos valores entre 0 e 10")
            continue
        
         else:
            turma[nome] = nota
            count += 1
        except ValueError:
         print("A nota deve ser numerica, e o nome alfabetico!")
         continue
          
               
def editar(turma : dict):
 while True:
    try:
        nome = input("digite o nome do aluno a ser editado: ")
        if turma[nome] != None:
         nota = input("digite a nota nova a ser atribuida: ")
        if not nota.isnumeric():
          print("a nota deve ser um numero")
          continue
        turma[nome] = nota
        break
    except KeyError:
          print("O aluno não existe!")
def excluir(turma: dict):
 while True:
    try:
         nome = input("digite o nome do aluno a ser excluido: ")
         if nome in turma:
            del turma[nome]
            break
         else:
            print("O aluno não existe!")
    except KeyError:
      print("O aluno não existe!")
      
   
def listar(turma: dict):
 print(turma)

def media(turma: dict):
    media = sum(turma.values()) / 10
    print(media)

def consultar(turma: dict):
  nome = input("digite o nome do aluno a ser consultado: ")
  if nome in turma:
    print(turma[nome])
  else:
   print("O aluno não existe!")

def apagar(turma: dict):
  turma.clear()
  print("turma apagada com sucesso!")
  return turma

   


while True:
 print("""Escolha uma opção
     1 - Adicionar novo Aluno 
     2 - Editar Aluno 
     3 - Listar os Alunos
     4 - Excluir um Aluno
     5 - Calcular a média da turma
     6 - Consultar um aluno
     7 - Apagar todos os alunos da sala
     8 - Sair
""")
 escolha = input("Escolha: ")

 match escolha:
    case "1":
     adicionar(turma)
    case "2":
     editar(turma)
    case "3":
     listar(turma)
    case "4":
     excluir(turma)
    case "5":
     media(turma)
    case "6":
     consultar(turma)
    case "7":
     apagar(turma)
    case "8":
     print("Saindo...")
     break   
    case _:
     print("Opção inválida!")
    


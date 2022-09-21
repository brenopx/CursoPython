"""
Aula 70
Faça uma lista de tarefas com as seguintes opções:
   adicionar tarefa
   listar tarefas
   opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
   opção de refazer (a cada vez que chamarmos, refaz a última ação)

   ['Tarefa 1', 'Tarefa 2']
   ['Tarefa 1'] <- Desfazer
   ['Tarefa 1', 'Tarefa 2'] <- Refazer

   input <- Nova Tarefa
"""
# def lista_de_comandos():
#     tarefas = []
#     ultimo = None
#     while True:
#         comando = input('Digite o seu comando: ')
#         if comando == 'adicionar':
#             tarefa = input('Digite qual tarefa voce quer acidionar: ')
#             # tarefa.extend([string])
#             tarefas.append(tarefa)
#             print(f"A tarefa {tarefa}, foi adicionada na lista {tarefas}")
#         elif comando == 'listar':
#             print(f"Voce tem essas {tarefas} tarefas")
#         elif comando == 'desfazer':
#             if tarefas == []:
#                 print('Voce não tem tarefas salvas')
#             else:
#                 ultimo = tarefas.pop()
#                 print(f"A tarefa {ultimo} foi removida")
#         elif comando == 'refazer':
#             if ultimo == None:
#                 print('Voce não tem tarefas salvas')
#                 continue
#             tarefas.append(ultimo)
#             print(f"A ultima tarefa removida foi {ultimo}
#             ela foi adicionada novamente")
#             ultimo = None
#         else:
#             print('Digite um comando valido')
# lista_de_comandos()


def show_op(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()


def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a desfazer')
        return
    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer')
        return
    last_redo = redo_list.pop()
    todo_list.append(last_redo)


def do_add(todo, todo_list):
    todo_list.append(todo)


if __name__ == '__main__':
    todo_list = []
    redo_list = []
    while True:
        todo = input('Digite uma tarefa ou undo, redo, ls: ')
        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list, redo_list)
            continue
        elif todo == 'redo':
            do_redo(todo_list, redo_list)
            continue
        do_add(todo, todo_list)

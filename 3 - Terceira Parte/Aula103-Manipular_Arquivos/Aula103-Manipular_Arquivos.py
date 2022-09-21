"""
Aula 103 - OS + SHUTIL - Mover, Copiar e Apagar Arquivos
"""
import os
# import shutil


caminho_original = '/home/breno/Projetos/CursoPython/Aula103'
caminho_novo = '/home/breno/Projetos/CursoPython/Aula103/Arquivos'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        # print(old_file_path)

        # if '.txt' in file:
        # shutil.move(old_file_path, new_file_path)
        # print(f'Arquivo {file} movido com sucesso!')

        # shutil.copy(old_file_path, new_file_path)
        # print(f'Arquivo {file} copiado com sucesso!')

        print(new_file_path)
        if '.txt' in file:
            os.remove(new_file_path)
            print(f'Arquivo {file} apagado com sucesso!')

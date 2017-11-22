#!/usr/bin/env python3.6
# encoding: utf-8
"""
Um pequeno utilitário para automatizar a cópia de segurança de uma determinada
pasta (por exemplo, cópias de segurança locais de uma base de dados Filemaker,
uma coleção de scripts e aplicações do Pythonista, etc.), criando arquivos 
*zip* individuais a partir de cada pasta principal nalocalização especificada e
fazendo *upload* dos mesmos para a Dropbox. O programa mantém um registo
simples, por forma a nao repetir as tarefas de compressão e upload já
realizadas.

© 2017 Victor Domingos (http://victordomingos.com)
Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
"""

import shutil
import datetime
import os
import os.path

import dropbox

from app_settings import INPUT_FOLDER, ARCHIVE_PATH, ARCHIVE_FILE_NAME
from app_settings import REMOTE_PATH, BACKUP_LOG_FILE, TOKEN


def obter_lista_de_pastas(register_file_path):
    """ Obtém do ficheiro de registo a lista das pastas já copiadas e compara
        essa lista com as pastas existentes no computador local. A função
        devolve a lista das pastas a arquivar e copiar.
    """
    print('A obter lista de pastas a copiar...')
    # Lista todas as subpastas na pasta principal (aqui designada como "raiz")
    raiz = os.path.expanduser(INPUT_FOLDER)
    pastas = ["{}{}{}".format(raiz, "/", pasta) for pasta in next(os.walk(raiz))[1]]
    
    # Obter do ficheiro a lista das pastas já tratadas e gerar lista sem essas

    lista_final = pastas     #TODO - retirar as pastas já presentes no ficheiro de registo
    print('\n\nLista depastas a copiar:\n', lista_final)
    return lista_final


def adiciona_registo(folder):
    """ Adiciona o caminho especificado ao ficheiro de registo. """
    print("\n\nAdicionando registo (TODO)") #TODO


def comprimir_pasta(origem, destino):
    """ Comprime a pasta de origem para o destino especificado. """
    print("\n\nA comprimir a cópia local...")
    try:
        print("Origem:", origem)
        print("Destino:", destino)
        arq = shutil.make_archive(destino, 'zip', root_dir=origem, base_dir=origem)
        return arq
    except Exception as e:
        print('\n\nOcorreu um erro durante a compressão:')
        print(e)
        return None
        

def upload_dropbox(archive, dropbox_path, token):
    """ Faz upload do ficheiro especificado para a Dropbox. """
    print("\n\nA fazer upload para a Dropbox...")
    try:
        dbx = dropbox.Dropbox(token)
        with open(archive, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path)
        return True
    except Exception as e:
        print('\n\nOcorreu um erro durante o upload para a Dropbox:')
        print(e)
        return None


def apagar_arquivo(archive):
    """ Apaga o ficheiro especificado no sistema de ficheiros local. """
    print("A apagar o ficheiro temporário local...")
    try:
        os.remove(archive)
    except Exception as e:
        print('\n\nOcorreu um erro ao apagar o arquivo zip:')
        print(e)


def main():
    backup_log_path = os.path.expanduser(BACKUP_LOG_FILE)
    dropbox_token = TOKEN
    
    for path in obter_lista_de_pastas(backup_log_path):
        timestamp = str(datetime.datetime.now())
        input_path = os.path.expanduser(path)
        archive_path = os.path.expanduser(ARCHIVE_PATH + ARCHIVE_FILE_NAME + timestamp)
        dropbox_archive_path = REMOTE_PATH + timestamp + ".zip"

        arquivo = comprimir_pasta(input_path, archive_path)

        if arquivo:
            if upload_dropbox(arquivo, dropbox_archive_path, dropbox_token):
                adiciona_registo(input_path)
            apagar_arquivo(arquivo)
    

if __name__ == "__main__":
    main()
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

import dropbox

#from app_settings import *
#from app_settings_iOS import *
from app_settings_Mac import *


def obter_registo(register_file_path):
    """ Obtém do ficheiro de registo a lista das pastas já copiadas. """
    pass


def comprimir_pasta(origem, destino):
    """ Comprime a pasta de origem para o destino especificado. """
    try:
        print("Origem:", origem)
        print("Destino", destino)
        arq = shutil.make_archive(destino, 'zip', origem)
        return arq
    except Exception as e:
        print('\n\nOcorreu um erro durante a compressão:')
        print(e)
        return None
        

def upload_dropbox(archive, dropbox_path, token):
    """ Faz upload do ficheiro especificado para a Dropbox. """
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
    try:
        pass #TODO
    except Exception as e:
        print('\n\nOcorreu um erro ao apagar o arquivo zip:')
        print(e)
        

def adiciona_registo(folder):
    """ Adiciona o caminho especificado ao ficheiro de registo. """
    pass


def main():
    timestamp = str(datetime.datetime.now())
    input_path = os.path.expanduser(INPUT_FOLDER)
    archive_path = os.path.expanduser(ARCHIVE_NAME + timestamp)
    dropbox_archive_path = REMOTE_PATH + timestamp + ".zip"
    backup_log_path = os.path.expanduser(BACKUP_LOG_FILE)
    dropbox_token = TOKEN


    arquivo = comprimir_pasta(input_path, archive_path)

    if arquivo:
        if upload_dropbox(arquivo, dropbox_archive_path, dropbox_token):
            adiciona_registo(input_path)
        apagar_arquivo(arquivo)
        pass # continue
    else:
        pass # continue


if __name__ == "__main__":
    main()

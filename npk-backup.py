#!/usr/bin/env python3.6
# encoding: utf-8
"""
Um pequeno utilitário para automatizar a cópia de segurança de uma determinada
pasta (por exemplo, cópias de segurança locais de uma base de dados Filemaker,
uma coleção de scripts e aplicações do Pythonista, etc.), criando arquivos
*zip* individuais a partir de cada pasta principal na localização especificada
e fazendo *upload* dos mesmos para a Dropbox. O programa mantém um registo
simples, por forma a não repetir as tarefas de compressão e upload já
realizadas. Em cada execução, são efetuadas cópias individuais de cada pasta
nova, que ainda não conste nas cópias anteriores. Não são contudo copiadas
pastas nem ficheiros previamente copiados, que possam ter sido alterados
entretanto.

© 2017 Victor Domingos (http://victordomingos.com)
Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
"""

import shutil
import datetime
import os
import os.path
import pickle
import logging
import logging.handlers


from pprint import pformat

import dropbox

from app_settings_Mac import INPUT_FOLDER, ARCHIVE_PATH
from app_settings_Mac import REMOTE_PATH, BACKUP_LOG_FILE, TOKEN, LOGS_PATH


logger = logging.getLogger()


def setup_logging():
    log_path = os.path.expanduser(LOGS_PATH)
    
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
    
    # Write log messages to a file
    file = logging.FileHandler(log_path)
    file.setLevel(logging.DEBUG)
    file.setFormatter(formatter)
    logger.addHandler(file)
    
    # Show log messages also on screen
    screen = logging.StreamHandler()
    screen.setLevel(logging.DEBUG)
    screen.setFormatter(formatter)
    logger.addHandler(screen)


def obter_lista_de_pastas(register_file_path):
    """ Obtém do ficheiro de registo a lista das pastas já copiadas e compara
        essa lista com as pastas existentes no computador local. A função
        devolve a lista das pastas a arquivar e copiar.
    """
    logger.debug('A obter lista de pastas existentes no armazenamento local...')
    # Lista todas as subpastas na pasta principal (aqui designada como "raiz")
    raiz = os.path.expanduser(INPUT_FOLDER)
    pastas_locais = ["{}{}".format(raiz, pasta)
                     for pasta in next(os.walk(raiz))[1]]

    # Obter do ficheiro a lista das pastas já tratadas e gerar lista sem essas
    logger.debug('A obter lista de pastas ja arquivadas...')
    try:
        with open(register_file_path, 'rb') as f:
            pastas_arquivadas = pickle.load(f)
    except Exception as e:
        pastas_arquivadas = []
        logger.debug('>>> Ocorreu um erro durante a leitura do registo:')
        logger.debug(str(e))

    lista_final = [pasta for pasta in pastas_locais
                   if pasta not in pastas_arquivadas]
    return lista_final


def adiciona_registo(register_file_path, path):
    """ Adiciona o caminho especificado ao ficheiro de registo. """
    logger.debug("Adicionando registo...")

    try:
        with open(register_file_path, 'rb') as f:
            pastas = pickle.load(f)
    except Exception as e:
        pastas = []
        logger.debug('>>> Ocorreu um erro durante a leitura do registo:')
        logger.debug(str(e))

    pastas.append(path)
    logger.debug(pformat(pastas))

    try:
        with open(register_file_path, 'wb') as f:
            pickle.dump(pastas, f)
    except Exception as e:
        logger.debug('>>> Ocorreu um erro durante a atualização do ficheiro de registo:')
        logger.debug(str(e))


def comprimir_pasta(origem, destino):
    """ Comprime a pasta de origem para o destino especificado. """
    try:
        logger.debug("A comprimir a copia local...")
        arq = shutil.make_archive(destino, 'zip', root_dir=origem)
        return arq
    except Exception as e:
        logger.debug('>>> Ocorreu um erro durante a compressao:')
        logger.debug(str(e))
        return None


def upload_dropbox(archive, dropbox_path, token):
    """ Faz upload do ficheiro especificado para a Dropbox. """
    try:
        logger.debug("A fazer upload para a Dropbox...")
        logger.debug(str(dropbox_path))
        dbx = dropbox.Dropbox(token)
        with open(archive, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path)
        return True
    except Exception as e:
        logger.debug('>>> Ocorreu um erro durante o upload para a Dropbox:')
        logger.debug(str(e))
        return None


def apagar_arquivo(archive):
    """ Apaga o ficheiro especificado no sistema de ficheiros local. """
    try:
        logger.debug("A apagar o ficheiro temporario local...")
        os.remove(archive)
    except Exception as e:
        logger.debug('>>> Ocorreu um erro ao apagar o arquivo zip:')
        logger.debug(str(e))


def main():
    backup_log_path = os.path.expanduser(BACKUP_LOG_FILE)
    dropbox_token = TOKEN
    
    setup_logging()

    lista_pastas_novas = obter_lista_de_pastas(backup_log_path)
    if lista_pastas_novas == []:
        logger.debug("Não ha pastas novas! A terminar a operacao.\n")
        return

    logger.debug("A iniciar procedimento de arquivo...\n======================")
    for path in lista_pastas_novas:
        logger.debug("--------- Pasta atual: ---------")
        logger.debug(path)
        timestamp = str(datetime.datetime.now())
        input_path = os.path.expanduser(path)
        hoje = datetime.datetime.now()
        ano, mes, dia = hoje.year, hoje.month, hoje.day

        archive_file_name = os.path.basename(os.path.normpath(os.path.expanduser(path)))
        archive_path = os.path.expanduser(ARCHIVE_PATH + archive_file_name + "____" + timestamp)
        dropbox_archive_path = "{}/{}/{}/{}/{}.zip".format(REMOTE_PATH,
                                                           ano, mes, dia,
                                                           archive_file_name + "____" + timestamp)

        arquivo = comprimir_pasta(input_path, archive_path)

        if arquivo:
            if upload_dropbox(arquivo, dropbox_archive_path, dropbox_token):
                adiciona_registo(backup_log_path, path)
            apagar_arquivo(arquivo)


if __name__ == "__main__":
    main()

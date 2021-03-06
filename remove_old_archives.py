#!/usr/bin/env python3
# encoding: utf-8
"""
Um pequeno utilitário complementar ao utilitário NPK-Backup, que serve para
automatizar a remoção de ficheiros de arquivo antigos na pasta especificada
(a utilizar numa máquina onde estejam alojada a pasta de arquivo sincronizada
com a Dropbox). Em cada execução, este programa apaga todas as pastas (e
respetivos conteúdos) cuja data seja mais recente do que o número de dias
indicado no ficheiro de configurações.

NOTA: Este script apaga de forma imediata e irreversível ficheiros e pastas,
sem qualquer aviso prévio ao utilizador, pelo que existe risco de perda de
dados. Recomenda-se por isso as devidas precauções e testes exaustivos antes de
decidir utilizá-lo num contexto real.

© 2017 Victor Domingos (http://victordomingos.com)
Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
"""

import os
import datetime
import shutil
import logging
import logging.handlers

from send2trash import send2trash

from app_settings_remove_old import BACKUPS_FOLDER, BACKUP_TIMEOUT
from app_settings_remove_old import USE_TRASH, LOGS_PATH


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


def delete_dir_by_date(main_path, year, month=None, day=None):
    full_path = '{}/{}'.format(main_path, year)
    if month is not None:
        full_path = '{}/{}'.format(full_path, month)
    if day is not None:
        full_path = '{}/{}'.format(full_path, day)

    if USE_TRASH:
        msg = 'Sending directory to Trash: ' + full_path
        logger.debug(msg)
        send2trash(full_path)
    else:
        msg = 'Deleting directory: ' + full_path
        logger.debug(msg)
        shutil.rmtree(full_path, ignore_errors=True, onerror=None)


def main():
    pasta_principal = os.path.expanduser(BACKUPS_FOLDER)
    timeout = datetime.datetime.now() - datetime.timedelta(days=BACKUP_TIMEOUT)
    ano, mes, dia = timeout.year, timeout.month, timeout.day

    setup_logging()

    for pasta_ano in os.listdir(pasta_principal):
        if pasta_ano.startswith('.'):
            continue
        try:
            if int(pasta_ano) < ano:
                delete_dir_by_date(pasta_principal, pasta_ano)
                continue
            elif int(pasta_ano) > ano:
                continue  # passa para a pasta de ano seguinte
        except Exception as e:
            msg = 'An exception occurred while iterating through the folders.\n' + str(e)
            logger.debug(msg)
            logger.debug("Continuing with next folder...")
            continue

        # se pasta_ano == ano, então continua a processar o seu conteúdo...
        pasta_ano_atual = pasta_principal + '/' + pasta_ano
        for pasta_mes in os.listdir(pasta_ano_atual):
            if pasta_mes.startswith('.'):
                continue
            try:
                if int(pasta_mes) < mes:
                    delete_dir_by_date(pasta_principal, pasta_ano, pasta_mes)
                    continue
                elif int(pasta_mes) > mes:
                    continue  # passa para a pasta de mes seguinte
            except Exception as e:
                msg = 'An exception occurred while iterating through the folders.\n' + str(e)
                logger.debug(msg)
                logger.debug("Continuing with next folder...")
                continue

            # se pasta_mes == mes, então continua a processar o seu conteúdo...
            pasta_mes_atual = pasta_principal + '/' + pasta_ano + '/' + pasta_mes
            for pasta_dia in os.listdir(pasta_mes_atual):
                if pasta_dia.startswith('.'):
                    continue
                try:
                    if int(pasta_dia) < dia:
                        delete_dir_by_date(pasta_principal, pasta_ano, pasta_mes, pasta_dia)
                except Exception as e:
                    msg = 'An exception occurred while iterating through the folders.\n' + str(e)
                    logger.debug(msg)
                    logger.debug("Continuing with next folder...")
                    continue


if __name__ == "__main__":
    main()

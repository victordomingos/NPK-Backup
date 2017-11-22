#!/usr/bin/env python3.6
# encoding: utf-8
"""
Este módulo é parte integrante da aplicação NPK-Backup, desenvolvida por
Victor Domingos e distribuída sob os termos da licença Creative Commons
Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
"""


# ------- Configurar estas variáveis antes de usar. ---------


# Caminho completo para a pasta que contém os ficheiros e pastas a arquivar e
# copiar (com '/' no final).
INPUT_FOLDER = '~/Desktop/Filemaker_backups/db-backup/'

# Caminho para o arquivo zip temporário a criar para o upload (com '/' no final).
ARCHIVE_PATH = '~/Desktop/tmp/'

# Caminho de destino na Dropbox para o arquivo a carregar (serão acrescentados no 
# final o carimbo de data/hora e a extensão '.zip'). Sem '/' no final.
REMOTE_PATH = '/backups'

# Caminho completo para o ficheiro de registo
BACKUP_LOG_FILE = '~/Documents/.backup-log.pkl'

# Token de acesso ao Dropbox
TOKEN = 'GetYourAppTokenFromDropboxAndInsertItHere'

# ----------------------------------------------------------

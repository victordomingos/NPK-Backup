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
INPUT_FOLDER = '~/Documents/NPK-Backup/db-backup-test/'

# Caminho para o arquivo zip temporário a criar para o upload (com '/' no final).
ARCHIVE_PATH = '~/Documents/NPK-Backup/tmp/'
ARCHIVE_FILE_NAME = "db-backup__"

# Caminho de destino na Dropbox para o arquivo a carregar (serão acrescentados no 
# final o carimbo de data/hora e a extensão '.zip'). Sem '/' no final.
REMOTE_PATH = '/backups/db-backup__'

# Caminho completo para o ficheiro de registo
BACKUP_LOG_FILE = '~/Documents/NPK-Backup/tmp/backup-log.pkl'

# Token de acesso ao Dropbox
TOKEN = 'GetYourAppTokenFromDropboxAndInsertItHere'

# ----------------------------------------------------------

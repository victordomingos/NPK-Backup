#!/usr/bin/env python3.6
# encoding: utf-8
"""
Este módulo é parte integrante da aplicação NPK-Backup, desenvolvida por
Victor Domingos e distribuída sob os termos da licença Creative Commons
Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
"""


# ------- Configurar estas variáveis antes de usar. ---------


# Caminho completo para a pasta que contém os ficheiros e pastas a arquivar e copiar.
INPUT_FOLDER = '~/Documents/NPK-Backup/db-backup-test/'

# Caminho para o arquivo zip temporário a criar para o upload.
ARCHIVE_PATH = '~/Documents/NPK-Backup/tmp/'
ARCHIVE_FILE_NAME = "db-backup__"

# Caminho de destino na Dropbox para o arquivo a carregar (serão acrescentados no 
# final o carimbo de data/hora e a extensão '.zip').
REMOTE_PATH = '/backups/db-backup__'

# Caminho completo para o ficheiro de registo de pastas previamente arquivadas
BACKUP_LOG_FILE = '~/Documents/NPK-Backup/backup-log.pkl'

# Caminho para o ficheiro de registo (informação de debugging)
LOGS_PATH = '~/Documents/NPK-Backup/npk-backup.log'

# Token de acesso ao Dropbox
TOKEN = 'GetYourAppTokenFromDropboxAndInsertItHere'

# ----------------------------------------------------------

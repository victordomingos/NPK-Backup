#!/usr/bin/env python3
# encoding: utf-8
"""
Este módulo é parte integrante da aplicação NPK-Backup, desenvolvida por
Victor Domingos e distribuída sob os termos da licença Creative Commons
Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
"""


# ------- Configurar estas variáveis antes de usar. ---------


# Caminho completo para a pasta que contém os ficheiros e pastas a arquivar e
# copiar (sem '/' no final).
BACKUPS_FOLDER = '~/Documents/NPK-Backup/delete-tests'

# Número de dias que as cópias de segurança devem ser conservadas sem apagar.
BACKUP_TIMEOUT = 5

# Usar 'Lixo'/'Reciclagem' do sistema operativo em vez de apagar imediatamente?
USE_TRASH = True

# ----------------------------------------------------------

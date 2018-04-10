#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import pexpect
import os
import datetime
import locale
import logging
import logging.handlers

from logging.handlers import TimedRotatingFileHandler

#locale.setlocale(locale.LC_ALL, "es_MX.UTF-8") #para user ñ y caracteres latinos

time.sleep(50)
ruta="/poner/ruta/a/folder/TXT"
rutat="/ruta/Donde/instalas/o/ejecutas/telegram-cli/tg/bin"
#now = datetime.datetime.now()
#fecha = now.strftime("%a %d %b %Y %H:%M:%S")
dif1 = [] #variable paa almacenar intrusas como lista python

tele = pexpect.spawn("%s/telegram-cli -k tg-server.pub -W -C" % rutat)
time.sleep(2)
#------------------------------


def archivo_log(dif):      #para crear el log con intrusos

    
    # Creamos una instancia al logger con el nombre especificado
    logger=logging.getLogger('*INTRUSOS*')
    
    # Indicamos el nivel maximo de seguridad para los mensajes que queremos que se
    # guarden en el archivo de logs
    # Los niveles son:
    #   DEBUG - El nivel mas alto
    #   INFO
    #   WARNING
    #   ERROR
    #   CRITIAL - El nivel mas bajo
    logger.setLevel(logging.DEBUG)
    
    # Creamos una instancia de logging.handlers, en la cual vamos a definir el nombre
    # de los archivos, la rotación que va a tener, y el formato del mismo
    
    # Si maxBytes=0, no rotara el archivo por tamaño
    # Si backupCount=0, no eliminara ningún fichero rotado
    #handler = logging.handlers.RotatingFileHandler(filename='file.log', mode='a', maxBytes=1024, backupCount=5)
    # MIO when= w0 es para rotar los lunes w1 martes, w2 miercoles, etc ,etc
    handler = TimedRotatingFileHandler('%s/intrusos.log' % ruta,
                                        when="w0",
                                        interval=1,
                                        backupCount=3) 
    
    # Definimos el formato del contenido del archivo de logs
    formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s \n\n\t%(message)s------------------------------------------------',datefmt='%a %d %b %Y %H:%M:%S,')
    
    # Añadimos el formato al manejador
    handler.setFormatter(formatter)
    
    # Añadimos el manejador a nuestro logging
    logger.addHandler(handler)
    
    # Añadimos mensajes al fichero de log
    #logger.info('\n-------------------------')
    logger.warning('%s \n' % dif)
    #logger.debug('message debug %s' % dif)
    #logger.info('message info %s' % dif)
    #logger.warning('message warning')
    #logger.error('message error')
    #logger.critical('message critical')


#----------------------------------------------------
with open('%s/devices.txt' % ruta) as f:
    t1 = f.read().splitlines()
    t1s = set(t1)

with open('%s/temp.txt' % ruta) as f:
    t2 = f.read().splitlines()
    t2s = set(t2)

for diff in t2s-t1s:
    time.sleep(1)
    dif1.append(diff)

if not dif1:             #checa si dif1 esta vacio
    print "SIN Intrusos" #solo para verificar si dif1 esta vacio

else:
    print "Inrusos en TEMP" #solo para efectos de verificacion
    tele.sendline('msg USER Reporte de INTRUSOS')
    time.sleep(1)
    tele.sendline("msg USER %s" % dif1)
    time.sleep(1)
    tele.sendline('quit')
    dif2 = "\n\t".join(str(x) for x in dif1)
    archivo_log(dif2)

  
print dif1 #solo para efectos de verificacion


# Intrusos en RED wifi/ethernet v0.2
Nueva version de esta herramienta, es la que actualmente uso


Buscar dispositivos en red y envíar aviso via TELEGRAM en caso de intrusos

Nueva version,en uso actualmente.

Desarrollada para RASPBERRY PI 2, aun que adaptabe a otros linux.

Escanea la red WIFI y ethernet.

Genera archivos log por dia, guarda solo 3 días para efectos de revisón y para no ocupar mucho espacio en disco. 

Version de desarrollo aun no publicada para su uso normal. 
Usala bajo tu propio riesgo (en realidad no tiene ningun riesgo :)   ) Se aceptan ideas

Se trata de escanear tu red en busca de los numeros MAC de los dispositivos conectados y compararlos con una lista de aquellos que reconoces y permites que se conecten. En caso de encontrar alguno que no esta en la lista te manda un aviso a travez de Telegram y registra la MAC del intruso en un archivo log.

Requiere:

python 2.7

Modulos python:

import sys

import time

import pexpect

import os

import datetime

import locale

import logging

import logging.handlers


Instalar Telegram-cli (linux) y verificar que funcione.

Instalar nmap (linux)

Agregar lineas al crontab (para efectos de que funcione todo el tiempo)

Conocer la ip de tu modem



Uso:

1.- Dar permisos de ejecutable al archivo intrusosWIFI.py



2.- En el archivo intrusosWIFI.py cambiar 

LINEA 18 

ruta="/poner/ruta/a/folder/TXT"

LINEA 19

rutat="/ruta/Donde/instalas/o/ejecutas/telegram-cli/tg/bin"

Cambiar USER en lineas 94 y 96, por el alias de un contacto que ya tengas de TELEGRAM al que le llagaran las alertas (puedes ser tu mismo)



3.- Poner MACs de dispositivos conocidos en el archivo devices.txt copiando y pegando la salida del siguiente comando mientras tus dispositivos estan canectados(posteriormente se pueden agragar mas):


[sudo nmap -sP ip.de.tu.modem/24 | grep MAC]



4.- Editar el cron del root con el siguiente comando (yo uso nano como editor):


sudo crontab -e


y pegar la siguiente linea al final(modifica la ruta):

*/10 * * * * nmap -n -sP -PA -PU ip.de.tu.modem/24|grep MAC > /ruta/donde/esta/archivo/TXT/temp.txt 2>&1


(este es el comando de nmap que me resulto mas util)



5.- Editar el cron del usuario con el siguiente comando (puede ser tambien el del root con sudo):

crontab -e


pegar la siguiente linea al final del archivo (modifica la ruta)


*/10 * * * * /usr/bin/python /ruta/donde/esta/el/archivo/intrusosWIFI.py > /dev/null 2>&1


Solo poner atención a las rutas pues el script, el crontab y Telegram-cli buscan los archivos en esas rutas

Con esto en los archivos cron se logra un escaneo de red cada 10 min , lo cual se puede modicar segun sus necesidades



NOTAS:


* Instalacion y uso de TELEGRAM-CLI >>> [(https://github.com/vysheng/tg)]



* Nota telegram-cli: 


Si les presenta el siguiente error al intentar ejecutar telegram-cli:

tgl/mtproto-utils.c:101: BN2ull: Assertion '0' failed.


Deben hacer un cambio en el archivo (buscar en su descaga de telegram-cli)

tgl/mtproto-utils.c, en la linea 101


assert (0); // As long as nobody ever uses this code, assume it is broken.

cambiar por :

//assert (0); // As long as nobody ever uses this code, assume it is broken.


es decir, se agregan dobles diagonales al inicio

y volver a hacer

make

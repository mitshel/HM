# Home Media catalog - Домашний медиа каталог
# Author: Dmitry V.Shelepnev
# Версия 0.01

## Что такое Home Media catalog
HMc - программа для каталогизации домашний архивов медиа-файлов. В первую очередь - фотоальбомы и семейные видеоролики.
Разработана для использования на NAS и небольших домашних Linux - серверов. Основным ее отличием от аналогичных каталогизаторов
является каталогизация путем сканирования структуры каталогов файлового архива, посредством которой уже создана схема хранения и
именования архивов.

### Как установить Home Media catalog

    pip3 install --upgrade pip
    pip3 install django
    pip3 install mysqlclient

### Настройка MySQL
Для работы каталога необходимо создать базу данных "hmc" и пользователя с необходимыми правами,
например следующим образом:

    mysql -uroot -proot_pass mysql
    mysql > create database if not exists hmc default charset=utf8;
    mysql > grant all on hmc.* to 'hmc'@'localhost' identified by '19hMc74';
    mysql > commit;
    mysql > ^C

### Создание администратора (суперпользователя):
Для начала работы и конфигурирования системы необходимо создать админстратора при помощи команды
manage.py createsuperuser, как указано ниже:

    python3 manage.py createsuperuser
    Username (leave blank to use 'mitshel'): mitshel
    Email address: mitshel@mail.ru
    Password:
    Password (again):
    Superuser created successfully.


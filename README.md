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
    pip3 install pillow
    
При установке mysqlclient может быть такая ошибка в Windows:  

    error: Unable to find vcvarsall.bat  
    
Решение:  
Execute the following command based on the version of Visual Studio installed:  

    Visual Studio 2010 (VS10): SET VS90COMNTOOLS=%VS100COMNTOOLS%
    Visual Studio 2012 (VS11): SET VS90COMNTOOLS=%VS110COMNTOOLS%
    Visual Studio 2013 (VS12): SET VS90COMNTOOLS=%VS120COMNTOOLS%


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

### Особенности настройки NGINX:
Особое внимание нужно уделить параметру uwsgi_buffers. При указанных ниже параметрах uWSGI сможет
передать в NGINX 1024k x 32 = 32Мб информации. Учитывая, что архивы коллекций могут занимать и большие объемы,
возможно это число нужно будет увеличить.
    server {
        listen       80;
        server_name  photo.dsnet.ru;
        root         /home/www/homemediacat/;
        # обслуживание медиа файлов и статики
        location /media  {
                 alias /home/www/homemediacat/media;  # расположение медиафайлов
        }
        location /static {
                 alias /home/www/homemediacat/static;  # расположение статики
        }

        location / {
                uwsgi_pass         unix:/var/run/uwsgi/uwsgi.sock;
                uwsgi_buffers      32                      1024k;
                include            uwsgi_params;

                uwsgi_param        UWSGI_CHDIR             /home/www/homemediacat;
                uwsgi_param        UWSGI_FILE              HM/wsgi.py;
        }

    }


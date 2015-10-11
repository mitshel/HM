# Home Media catalog - �������� ����� �������
# Author: Dmitry V.Shelepnev
# ������ 0.01

## ��� ����� Home Media catalog
HMc - ��������� ��� ������������� �������� ������� �����-������. � ������ ������� - ����������� � �������� �����������.
����������� ��� ������������� �� NAS � ��������� �������� Linux - ��������. �������� �� �������� �� ����������� ���������������
�������� ������������� ����� ������������ ��������� ��������� ��������� ������, ����������� ������� ��� ������� ����� �������� �
���������� �������.

### ��� ���������� Home Media catalog

    pip3 install --upgrade pip
    pip3 install django
    pip3 install mysqlclient

### ��������� MySQL
��� ������ �������� ���������� ������� ���� ������ "hmc" � ������������ � ������������ �������,
�������� ��������� �������:

    mysql -uroot -proot_pass mysql
    mysql > create database if not exists hmc default charset=utf8;
    mysql > grant all on hmc.* to 'hmc'@'localhost' identified by '19hMc74';
    mysql > commit;
    mysql > ^C

### �������� �������������� (�����������������):
��� ������ ������ � ���������������� ������� ���������� ������� ������������� ��� ������ �������
manage.py createsuperuser, ��� ������� ����:

    python3 manage.py createsuperuser
    Username (leave blank to use 'mitshel'): mitshel
    Email address: mitshel@mail.ru
    Password:
    Password (again):
    Superuser created successfully.


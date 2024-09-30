#!/usr/bin/python3
import datetime
from dotenv import load_dotenv
import logging
import configargparse

import asyncio
import aiofiles
from socket import socket


async def write_to_file(file_name, text):
    '''
    Записывает текст в файл
    :param file_name: Путь к файлу
    :param text: Текст
    :return:
    '''
    async with aiofiles.open(file_name, 'a') as file:
        await file.write(text)


async def send_message_server(host, port, file_name='log.txt'):
    '''
    Программа отправляет сообщения Хосту.
    :param host: Хост или IP-адрес Хоста
    :param port: Порт Хоста
    :param file_name: Путь к файлу для записи истории переписок
    :return:
    '''
    pass


# async def main():
#     pass

if __name__ == '__main__':
    load_dotenv()
    description = ('Программа слушает Хост и порт. \n'
                   'Необходимо указать параметр \n'
                   '\t-H (--host) имя хоста или IP-адрес \n'
                   '\t-p (--port) номер порта \n',
                   '\t--history путь к файлу для записи истории переписок \n'
                   '\t--token токен пользователя для отправки сообщений \n')
    parser = configargparse.ArgParser(
        description=description,
        epilog='Пример: python3 main.py -H minechat.dvmn.org -p 5000 --history ./log.txt --token <YOUR_TOKEN>',
        default_config_files=['.env',]
    )
    parser.add('-H','--host', required=True,
               help='адрес хоста или IP-адрес',
               env_var='HOST')
    parser.add('-p', '--port', required=True,
               help='Номер порта',
               env_var='SEND_PORT')
    parser.add('--history', required=True,
               help='Путь к файлу для записи истории переписок',
               env_var='HISTORY')
    parser.add('--token', required=True,
               help='Токен пользователя для отправки сообщений',
               env_var='TOKEN')
    args, _ = parser.parse_known_args()

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


async def listen_server(host, port, file_name='log.txt'):
    '''
    Программа слушает Хост и порт.
    :param host: Хост или IP-адрес Хоста
    :param port: Порт Хоста
    :param file_name: Путь к файлу для записи истории переписок
    :return:
    '''
    while True:
        try:
            reader, _ = await asyncio.open_connection(host, port)
            line = await reader.readline()
            if line:
                timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M]")
                log = f'{timestamp} {line.decode()}'
                await write_to_file(file_name, log)
        except socket.gaierror as exe:
            print(f'Адрес {host} недоступен. Ошибка: {exe}')
            await asyncio.sleep(5)


# async def main():
#     pass

if __name__ == '__main__':
    load_dotenv()
    description = ('Программа слушает Хост и порт. \n'
                   'Необходимо указать параметр \n'
                   '\t-H (--host) имя хоста или IP-адрес \n'
                   '\t-p (--port) номер порта \n',
                   '\t--history путь к файлу для записи истории переписок \n')
    parser = configargparse.ArgParser(
        description=description,
        epilog='Пример: python3 main.py -H minechat.dvmn.org -p 5000 --history ./log.txt',
        default_config_files=['.env', ]
    )
    parser.add('-H', '--host', required=True,
               help='адрес хоста или IP-адрес',
               env_var='HOST')
    parser.add('-p', '--port', required=True,
               help='Номер порта',
               env_var='SEND_PORT')
    parser.add('--history', required=True,
               help='Путь к файлу для записи истории переписок',
               env_var='HISTORY')
    args = parser.parse_args()
    asyncio.run(listen_server(args.host, args.port))

#!/usr/bin/python3
from dotenv import load_dotenv
import logging
import configargparse

import asyncio
from socket import socket

from history import History


def init_config():
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
               env_var='RECEIVE_PORT')
    parser.add('--history', required=True,
               help='Путь к файлу для записи истории переписок',
               env_var='HISTORY')
    args, _ = parser.parse_known_args()
    return args


async def listen_server(host, port):
    '''
    Программа слушает Хост и порт.
    :param host: Хост или IP-адрес Хоста
    :param port: Порт Хоста
    :param file_name: Путь к файлу для записи истории переписок
    :return:
    '''
    reader, _ = await asyncio.open_connection(host, port)
    received_msg = await reader.readline()
    decode_msg = received_msg.decode()
    return decode_msg


async def main():
    config = init_config()
    history = History(config.history, print_history=True)
    while True:
        try:
            msg = await listen_server(config.host, config.port)
            await history.append(msg)
        except socket.gaierror:
            await asyncio.sleep(2)


if __name__ == '__main__':
    load_dotenv()
    asyncio.run(main())

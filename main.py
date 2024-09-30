import os
import argparse
import datetime
from dotenv import load_dotenv
import logging

import asyncio
import aiofiles
from socket import socket


async def write_to_file(file_name, text):
    async with aiofiles.open(file_name, 'a') as file:
        await file.write(text)



async def listen_server(host, port, file_name='log.txt'):

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
                   '\t-f (--file) имя файла для логирования')
    parser = argparse.ArgumentParser(
        prog='XChat',
        description=description,
        epilog='Пример: python3 main.py -H minechat.dvmn.org -p 5000'
    )
    parser.add_argument('-H','--host',
                        type=str, default='minechat.dvmn.org',
                        help='адрес хоста или IP-адрес',)
    parser.add_argument('-p', '--port',
                        type=int, default=5000,
                        help='Номер порта')
    parser.add_argument('-f', '--file',
                        type=str, default="log.txt",
                        help='Файл для логирования')
    args = parser.parse_args()
    asyncio.run(listen_server(args.host, args.port))

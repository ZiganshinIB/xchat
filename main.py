import asyncio
import argparse
from dotenv import load_dotenv


async def listen_server(host, port):
    while True:
        reader, writer = await asyncio.open_connection(host, port)
        line = await reader.readline()
        print(line.decode(), end='')


async def main():
    asyncio.run()

if __name__ == '__main__':
    load_dotenv()
    description = ('Программа слушает Хост и порт. \n'
                   'Необходимо указать параметр \n'
                   '\t-H (--host) имя хоста или IP-адрес \n'
                   '\t-p (--port) номер порта')
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
    args = parser.parse_args()
    asyncio.run(listen_server(args.host, args.port))

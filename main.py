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
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default='minechat.dvmn.org')
    parser.add_argument('--port', type=int, default=5000)
    args = parser.parse_args()
    asyncio.run(listen_server(args.host, args.port))

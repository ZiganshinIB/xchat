import datetime
import aiofiles


class History:
    def __init__(self, file_name, timeformat='[%Y-%m-%d %H:%M]', print_history=False):
        self.file_name = file_name
        self.history = []
        self.timeformat = timeformat
        self.print_history = print_history

    async def append(self, text):
        if self.print_history:
            print(text, end='')
        if self.timeformat:
            histr = f'{datetime.datetime.now().strftime(self.timeformat)}\t{text}'
        else:
            histr = f'{text}'
        async with aiofiles.open(self.file_name, 'a') as file:
            await file.write(histr)
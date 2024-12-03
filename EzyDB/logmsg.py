import time
import shutil
from textPlay.colors import *
from typing import Any

class Status:
    INFO = f"{BG_BLUE}{WHITE} INFO {RESET}"
    ERROR = f"{BG_RED}{WHITE} ERROR {RESET}"
    WARN = f"{BG_YELLOW}{BLACK} WARN {RESET}"
    DONE = f"{BG_GREEN}{BLACK} DONE {RESET}"    


def log(message, status:Status|Any , add_time: bool = True, print_able:bool= True):

    ctime = time.strftime("%I:%M %p")
    term = shutil.get_terminal_size().columns

    space = lambda: 9 if status==Status.ERROR else 8
    set_time = f"{DIM}{ctime if add_time else ''}{RESET}"

    if not print_able:
        return f" {status} {message}{' '* (term - len(ctime) - len(message) - 6)}{ctime if add_time else ''}"
    
    print(f" {status} {message}{' '* (term - len(ctime) - len(message) - space())}{set_time}")
    
    
class Logger:
    def __init__(self) -> None:
        pass
        
    def config(self, **kwargs):
        settings = kwargs
        self.add_time = settings.get("add_time", True)
        self.print_able = settings.get("print_able", True)

    def info(self, message):
        log(message, Status.INFO, self.add_time, self.print_able)
        
    def error(self, message):
        log(message, Status.ERROR, self.add_time, self.print_able)
        
    def warn(self, message):
        log(message, Status.WARN, self.add_time, self.print_able)
        
    def done(self, message):
        log(message, Status.DONE, self.add_time, self.print_able)
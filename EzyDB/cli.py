import click
import sys
import textPlay as tp
from textPlay.colors import *
import importlib
import threading
from logmsg import Logger
from plugin import git_fetch
from textPlay import progress_bar_loader
import subprocess

log = Logger()
log.config(add_time=True, print_able=True)


def install(cmd:str):
    loader = progress_bar_loader(symbol='█', empty_symbol='-', color_on_completion=GREEN)

    stop_thread = threading.Event()
    thread = threading.Thread(target=loader, args=(stop_thread,), daemon=True)
    thread.start()

    result = subprocess.run(cmd.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    stop_thread.set()
    thread.join()

    print()
    if result.returncode == 0:
        log.done(f"Successfully installed {cmd.split(' ')[-1]}")
    else:
        log.error(f"Failed to install {cmd.split(' ')[-1]}")

    return

def is_package_installed(package_name):
    """
    Checks whether a package is installed in the current Python environment.

    Args:
        package_name (str): The name of the package to check.

    Returns:
        bool: True if the package is installed, False otherwise.
    """
    try:
        importlib.import_module(package_name)
        return True
    except ModuleNotFoundError:
        return False
    
    

@click.group()
def cli():
    pass

def playground():
    if is_package_installed("EzyDB-cli"):
        tp.backend_exec("EzyDB-cli")
    else:
        log.error("EzyDB-cli is not installed")
        chose = input(f"\n:: Do you want to install it? (y/n){BLUE}[y]{RESET}: ")
        if chose.lower() == "y":
            data = git_fetch("cli")
            n, v = data["name"], data["version"]
            install(f"pip install {n}=={v}")
        else:
            log.info("You have chosen not to install EzyDB-cli")
            sys.exit()

def plugins():
    all_plugins = git_fetch("plugins")
    plugins = all_plugins["data_format"]
    cli = all_plugins["cli"]
    print("\nPlugins:")
    for plugin in plugins:
        print("•", plugin)

    print("\nCLI:")
    for plugin in cli:
        print("•", plugin)

plugins() 
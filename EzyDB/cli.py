import click
import sys
import textPlay as tp
from textPlay.colors import *
import importlib
import threading
from .logmsg import Logger
from .plugin import git_fetch
from textPlay import progress_bar_loader
import subprocess
import itertools
import time

log = Logger()
log.config(add_time=True, print_able=True)

@click.group()
def cmd_cli():
    """
    EzyDB CLI tool entry point.
    """
    print("\n\tEzyDB CLI\n")

install_animation = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
def spinner_animation(stop_event):
    spinner = itertools.cycle(install_animation)
    while not stop_event.is_set():
        sys.stdout.write(next(spinner))  # Write the next spinner character
        sys.stdout.flush()               # Force the character to display
        time.sleep(0.1)                  # Wait a bit before the next character
        sys.stdout.write('\b')           # Backspace to overwrite the character

    # Clear the spinner when stopping
    sys.stdout.write(' ')  # Write a space to clear the spinner
    sys.stdout.write('\b') # Move back again to overwrite the space with the next output

def install_package(cmd: str):
    """
    Install a package using pip with progress indication.

    Args:
        cmd (str): The pip install command.
    """
    try:

        stop_thread = threading.Event()
        thread = threading.Thread(target=spinner_animation, args=(stop_thread,), daemon=True)
        thread.start()

        result = subprocess.run(cmd.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        stop_thread.set()
        thread.join()

        print()
        if result.returncode == 0:
            log.done(f"Successfully executed: {cmd}")
        else:
            log.error(f"Command failed: {cmd}")
    except Exception as e:
        log.error(f"Error during installation: {e}")

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

def get_plugins():
    """
    Fetches and displays available plugins from the GitHub repository.
    """
    try:
        all_plugins:dict = git_fetch("plugins")
        plugins = all_plugins.get("data_format", [])
        cli = all_plugins.get("cli", [])
        print("\nPlugins:")
        for plugin in plugins:
            print("•", plugin, "Formatter")

        print("\nCLI:")
        for plugin in cli:
            print("•", plugin)
    except Exception as e:
        log.error(f"Failed to fetch plugins: {e}")

@click.command()
def playground():
    """
    Runs the EzyDB CLI playground.
    """
    if is_package_installed("EzyDB-cli"):
        tp.backend_exec("EzyDB-cli")
    else:
        log.error("EzyDB-cli is not installed")
        chose = input(f"\nDo you want to install it? (y/n){BLUE}[y]{RESET}: ")
        if chose.lower() == "y":
            data = git_fetch("cli")
            if data:
                n, v = data.get("name"), data.get("version")
                if n and v:
                    install_package(f"pip install {n}=={v}")
                else:
                    log.error("Invalid plugin data fetched")
            else:
                log.error("Failed to fetch CLI plugin data")
        else:
            log.info("You have chosen not to install EzyDB-cli")
            sys.exit(1)

@click.command()
@click.option("--plugin", "-p", help="Plugin to install", required=False)
@click.option("--all", "-a", help="Install all plugins", is_flag=True, required=False)
def install(plugin=None, all=False):
    """
    Installs specified plugins or all available plugins.
    """
    try:
        if plugin:
            plg = git_fetch(plugin.lower())
            if plg:
                print(f"Installing {plg['name']} {plg['version']}")
                install_package(f"pip install {plg['name']}=={plg['version']}")
            else:
                log.error(f"Plugin '{plugin}' not found")
        elif all:
            all_plugins = git_fetch("plugins", "data_format")
            if all_plugins:
                for plugin in all_plugins:
                    plg = git_fetch(plugin.lower())
                    if plg:
                        print(f"Installing {plg['name']} {plg['version']}")
                        install_package(f"pip install {plg['name']}=={plg['version']}")
                    else:
                        log.error(f"Plugin '{plugin}' not found")
            else:
                log.error("No plugins found to install")
        else:
            log.error("You have to choose a plugin to install")
    except Exception as e:
        log.error(f"Failed to process install command: {e}")

@click.command()
@click.option("--plugin", "-p", help="Plugin to update", required=False)
def update(plugin:str=None):
    """
    Updates a specified plugin or the main EzyDB package.
    """
    try:
        if plugin:
            plg = git_fetch(plugin.lower())
            if plg:
                print(f"Updating {plg['name']} {plg['version']}")
                install_package(f"pip install --upgrade {plg['name']}=={plg['version']}")
            else:
                log.error(f"Plugin '{plugin}' not found")
        else:
            install_package("pip install --upgrade EzyDB")
    except Exception as e:
        log.error(f"Failed to process update command: {e}")

cmd_cli.add_command(playground)
cmd_cli.add_command(install)
cmd_cli.add_command(update)

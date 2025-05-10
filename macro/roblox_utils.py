import webbrowser
import time
import pyautogui as pag

from discord_utils import detailed_report
from windows_utils import getWindowsWithTitle
from data import PRIVATE_SERVER_LINK


def close_roblox_windows():
    detailed_report('closing roblox windows..')
    for window in getWindowsWithTitle("Roblox"):
        window.close()

def open_roblox():
    detailed_report('opening roblox..')
    webbrowser.open(PRIVATE_SERVER_LINK)

def wait_for_roblox():
    # wait for roblox to open
    detailed_report('waiting for roblox to open..')
    while True:
        hwnd = getWindowsWithTitle("Roblox")
        if hwnd:
            hwnd[0].activate()
            break
        time.sleep(1)
    detailed_report('roblox opened!')

def wait_for_game():
    # wait for game to load
    detailed_report('waiting for game to load..')
    while True:
        if pag.pixel(946, 703) == (0, 0, 0) and pag.pixel(964, 798) == (255, 255, 255):
            break
        time.sleep(1)
    detailed_report('game loaded!')

def config_roblox_window():
    pass
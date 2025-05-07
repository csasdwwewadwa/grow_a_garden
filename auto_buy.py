import pyautogui as pag
import time
from ahk import AHK
import csamacro
import keyboard
import requests
import pygetwindow as gw
import webbrowser
import subprocess

ahk = AHK()
ahk.set_coord_mode('Mouse', 'Screen')

# -------------------------------
# discord webhook stuff
#

DETAILED_REPORT = True


USER = 'csa'
WEBHOOK_URL = {
    'csa': r'https://discord.com/api/webhooks/1369105978460606518/CFod8Iw2JDKwnFMkWVKHoC6I3KiCHrQqrKzZtuK2KoTOf-lFz6HK9tfDYd45jell7gRy',
    'cala': r'https://discord.com/api/webhooks/1369481930034118727/T8xo0aftValtBKwaMmc0Y47zro5zyC_Cf9lBw72wfzx30EwK1lsKDv5lV3gTL9oCwy6t',
}
PING = {
    'csa': '<@727017345356398592>',
    'cala': '<@1126918769512554507>'
}

def send_discord_message(content, webhook_url):
    payload = {
        "content": content
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(webhook_url, json=payload, headers=headers)

    if response.status_code != 204 and response.status_code != 200:
        print(f"Failed to send message: {response.status_code} - {response.text}")


def report(msg, is_ping=False):
    content = msg
    if is_ping:
        content += f' {PING[USER]}'
    send_discord_message(content, WEBHOOK_URL[USER])


def detailed_report(msg):
    if DETAILED_REPORT:
        report('-# ' + msg)

def report_rare_stuf(msg):
    RARE_STUF_WEBHOOK_URL = r'https://discord.com/api/webhooks/1369500156734476379/FTEzjUxhIkB-iFlsAgSRp__utMqVjEjJbiedZ0S3uFlj6AOva89S0_SmqicSJsfhGg7j'
    send_discord_message(msg, RARE_STUF_WEBHOOK_URL)


# -------------------------------
# general windows stuffs

PRIVATE_SERVER_LINK = r'https://www.roblox.com/share?code=22cba0e039f01f4cb24eabdc5fab7113&type=Server'

def getWindowsWithTitle(title):
    windows = []
    for window in gw.getAllWindows():
        if window.title == title:
            windows.append(window)
    return windows

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
        if hwnd and hwnd[0].isActive:
            break
        time.sleep(1)

    # wait for game to load
    detailed_report('waiting for game to load..')
    while True:
        if pag.pixel(946, 703) == (0, 0, 0) and pag.pixel(964, 798) == (255, 255, 255):
            break
        time.sleep(1)
    detailed_report('game loaded!')

def config_roblox_window():
    # window only need to be configed for cala
    if USER == 'cala':
        pass

# -------------------------------
# additional stuffs


def click_wait(x, y=None, wait=0.3):
    if type(x) == 'tuple':
        x, y = x
    ahk.click(x, y)
    time.sleep(wait)


NUM_UNIQUE_SEEDS = 17 # Amount of unique seeds sold in shop


def scroll_up(amount=1):
    for _ in range(amount):
        ahk.run_script('Send {WheelUp}')

def scroll_down(amount=1):
    for _ in range(amount):
        ahk.run_script('Send {WheelDown}')

def key_hold(key, duration=1):
    '''
    Hold a key for a certain duration
    '''
    ahk.key_down(key)
    time.sleep(duration)
    ahk.key_up(key)


# -------------------------------
# GAME UTILS YAYAYEAYEYA


def is_disconnected():
    return pag.pixel(1100, 429) == (57, 59, 61)


def rotate_camera(x, y):
    CAMERA_SENSITIVITY = 0.5
    csamacro.mouse_move_absolute(1500, 115)
    csamacro.mouse_move_relative(0, 5)
    csamacro.mouse_move_relative(0, -5)
    csamacro.mouse_button_down('right')
    csamacro.mouse_button_up('right')
    csamacro.mouse_button_down('right')
    csamacro.mouse_move_relative(round(x/CAMERA_SENSITIVITY*2), round(-y/CAMERA_SENSITIVITY*2), debounce=0.1)
    csamacro.mouse_button_up('right')
    csamacro.mouse_move_absolute(1500, 115)


def get_weather():
    def is_thunderstorm():
        return pag.pixel(1888, 997) == (255, 255, 127)

    def is_blizzard():
        return pag.pixel(1890, 1001) == (123, 233, 255)

    def is_rain():
        return pag.pixel(1890, 1007) == (0, 170, 255)
    
    if is_thunderstorm():
        return 'thunderstorm'
    elif is_blizzard():
        return 'blizzard'
    elif is_rain():
        return 'rain'
    else:
        return None

def tp_seed():
    click_wait(679, 137)

def get_egg_rarity():
    if pag.pixel(798, 366) == (255, 255, 255):
        return 'common'
    elif pag.pixel(798, 360) == (211, 167, 129):
        return 'uncommon'
    elif pag.pixel(799, 367) == (33, 84, 185):
        return 'rare'
    elif pag.pixel(798, 360) == (213, 255, 134):
        return 'bug'
    else:
        return 'unknown'


# -------------------------------
# SETUP N STUFF YAYEYREAYYR


def setup_camera():
    tp_seed()
    time.sleep(0.3)
    rotate_camera(0, -1000) # to top_down
    csamacro.mouse_scroll(-25) # zoom all out
    csamacro.mouse_scroll(5, debounce=0.3) # zoom in a bit
    
    # check for default camera position
    pxr = pag.pixel(1714, 628)
    pxl = pag.pixel(270, 628)
    pxur = pag.pixel(1509, 258)
    pxul = pag.pixel(407, 158)

    # case 1: 90
    if pxr[1] - pxr[2] < 70:
        rotate_camera(90, 0)
    
    # case 2: -90
    elif pxl[1] - pxl[2] < 70:
        rotate_camera(-90, 0)

    # case 3: 30.5
    elif pxur[1] - pxur[2] < 70:
        rotate_camera(30.5, 0)

    # case 4: -30.5
    elif pxul[1] - pxul[2] < 70:
        rotate_camera(-30.5, 0)
            
def setup_shops():
    # move to gear shop thing
    ahk.key_press('shift')
    key_hold('s', 17)
    ahk.key_press('shift')

    # prepare gear shop ui
    ahk.key_press('e')
    time.sleep(4)
    ahk.mouse_move(1027, 518)
    ahk.click(1090, 518)
    time.sleep(2) # wait for shop ui

    # snap to rod
    for _ in range(4):
        ahk.mouse_move(733, 873)
        click_wait(987, 873)

    ahk.click(1288, 264) # close diag


# -------------------------------wddd

def buy_seeds():
    def _to_next_item():
        ahk.mouse_move(733, 873)
        click_wait(987, 873)
    
    # first item init
    click_wait(679, 454)

    # main loop
    for seed_id in range(NUM_UNIQUE_SEEDS-1): # -1 because we are already on the first item
        buy_button_coord = (667, 634 + int(177 * (seed_id / (NUM_UNIQUE_SEEDS-1))))

        # check if the item is stocked (buyable)
        while pag.pixel(*buy_button_coord)[0] in (38, 29):
            # buy the item lol
            click_wait(buy_button_coord)
            continue

        # go to next item
        _to_next_item()

    # do pepper cuz lol
    ahk.click(774, 800) # click once so roblox register the mouse position properly
    scroll_down(1)
    time.sleep(0.3) # wait a bit to load
    click_wait(667, 835) # select pepper
    click_wait(667, 824) # buy pepper

    # move to first item
    ahk.mouse_move(1308, 814)
    ahk.mouse_drag(1308, 300, from_position=(1308, 864))

def buy_gears():
    click_wait(982, 348) # select godly sprinkler
    click_wait(974, 344) # select advanced sprinkler
    click_wait(776, 668) # buy advanced sprinkler
    click_wait(776, 668) # buy advanced sprinkler
    click_wait(933, 813) # select godly sprinkler
    click_wait(768, 677) # buy godly sprinkler
    click_wait(768, 677) # buy godly sprinkler
    click_wait(969, 831) # select rod
    click_wait(770, 687) # buy rod
    click_wait(960, 820) # select master sprinkler
    click_wait(765, 811) # buy master sprinkler
    click_wait(968, 394) # select rod

def buy_pet():
    # skip common egg.
    if get_egg_rarity() not in ('common', 'uncommon', 'rare'):
        click_wait(888, 679)
    click_wait(1304, 367)


# -------------------------------wddd

def main_iteration():
    # buy seeds
    buy_seeds()
    time.sleep(0.5) # wait a bit idk
    ahk.click(1288, 264) # close seed buy ui

    # move to gear shop thing
    ahk.key_press('shift')
    key_hold('s', 17)
    ahk.key_press('shift')

    # prepare gear shop ui
    ahk.key_press('e')
    time.sleep(4)
    ahk.mouse_move(1027, 518)
    ahk.click(1090, 518)
    time.sleep(2) # wait for shop ui

    # buy gears
    buy_gears()
    ahk.click(1288, 264) # close diag

    # buy pets
    key_hold('w', 0.2)
    key_hold('d', 1.2)
    ahk.key_press('e')
    time.sleep(0.3)
    buy_pet()
    key_hold('d', 0.22)
    ahk.key_press('e')
    time.sleep(0.3)
    buy_pet()
    key_hold('d', 0.22)
    ahk.key_press('e')
    time.sleep(0.3)
    buy_pet()

    # prepare seeds ui
    tp_seed()
    time.sleep(1)
    ahk.key_press('e')
    time.sleep(2) # wait for seeds ui


def main_loop():
    while True:
        # start new roblox instance
        close_roblox_windows()
        time.sleep(1)
        open_roblox()
        time.sleep(10)
        wait_for_roblox()
        report('Joined game!', is_ping=True)

        detailed_report('configing roblox window..')
        config_roblox_window()
        time.sleep(1)

        # setup
        ahk.click(1570, 150) # close the start uh window thing
        time.sleep(2)

        detailed_report('setting up camera..')
        setup_camera()
        detailed_report('setting up shops..')
        setup_shops()

        # move to start position
        tp_seed()
        time.sleep(1)
        ahk.key_press('e')
        time.sleep(2) # wait for seeds ui

        # main loop where i buy brrrt grin grind yayayeyeay
        report('Finished setup! Starting main loop..')
        while True:
            if is_disconnected():
                report('**Disconnected!** Attempting to rejoin...', is_ping=True)
                break
            main_iteration()
            time.sleep(150)


def main():
    report('## Started')
    main_loop()



# -------------------------------wddd

# MAIN CODE OMAG 


hotkey = '-'
print(f'REMEMBER TO HAVE GEARS DIALOG SETUP.\n'*4)
print(f'ready. Press "{hotkey}" to run.')

keyboard.add_hotkey(hotkey, main)
keyboard.wait()
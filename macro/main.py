import time
import keyboard


from game_utils import *
from discord_utils import *
from roblox_utils import *



NUM_UNIQUE_SEEDS = 17

def buy_seeds():
    def _to_next_item():
        ahk.mouse_move(733, 873)
        click_wait(987, 873)
    
    # first item init
    click_wait(679, 454)

    # main loop
    for seed_id in range(NUM_UNIQUE_SEEDS-1): # -1 because we are already on the first item
        buy_button_coord = (667, 634 + int(seed_id * 11.0625))

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

def buy_pets():
    def buy_pet():
        # skip L eggs.
        if get_egg_rarity() not in ('common', 'uncommon', 'rare'):
            click_wait(888, 679)
        click_wait(1304, 367)
        
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
    buy_pets()

    # prepare seeds ui
    tp_seed()
    time.sleep(1)
    ahk.key_press('e')
    time.sleep(2) # wait for seeds ui

def alt_iteration():
    pass


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
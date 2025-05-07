import pyautogui as pag
import time
from ahk import AHK
import keyboard


ahk = AHK()
ahk.set_coord_mode('Mouse', 'Screen')


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

def tp_seed():
    ahk.click(676, 141)



# egg


def is_egg_common():
    return pag.pixel(799, 374) == (255, 255, 255)

def is_egg_uncommon():
    return pag.pixel(793, 370) == (211, 167, 129)


# -------------------------------wddd

def buy_seeds():
    def _to_next_item():
        ahk.mouse_move(733, 873)
        ahk.click(987, 883)
    
    # first item init
    ahk.click(679, 454)
    time.sleep(0.3) # wait a bit to load

    # main loop
    for seed_id in range(NUM_UNIQUE_SEEDS-1): # -1 because we are already on the first item
        buy_button_coord = (667, 634 + int(176 * (seed_id / (NUM_UNIQUE_SEEDS-1))))

        # check if the item is stocked (buyable)
        while pag.pixel(*buy_button_coord)[0] in (38, 29):
            # buy the item lol
            ahk.click(buy_button_coord[0] + 70, buy_button_coord[1])
            time.sleep(0.2)
            continue

        # go to next item
        _to_next_item()
        time.sleep(0.3) # wait a bit to load

    # do pepper cuz lol
    ahk.click(774, 800)
    scroll_down(1)
    time.sleep(0.3) # wait a bit to load
    ahk.click(667, 835) # select pepper
    time.sleep(0.3) # wait a bit to load
    ahk.click(667, 824) # buy pepper
    time.sleep(0.3) # wait a bit to load

    # move to first item
    ahk.mouse_move(1308, 832)
    ahk.mouse_drag(1308, 300, from_position=(1308, 866))

def buy_gears_idk_2nd():
    ahk.click(771, 689) # buy rod
    ahk.click(719, 347) # select godly sprinkler
    time.sleep(0.3)
    ahk.click(770, 679) # buy godly sprinkler
    ahk.click(963, 821) # select rod
    time.sleep(0.3)
    ahk.click(941, 838) # select master sprinkler
    time.sleep(0.3)
    ahk.click(772, 815) # buy master sprinkler
    ahk.click(972, 413) # select rod
    time.sleep(0.3)

def buy_pet():
    if not (is_egg_common() or is_egg_uncommon()):
        ahk.click(888, 679)
        time.sleep(0.3)
    ahk.click(1304, 367)
    time.sleep(0.3)


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
    ahk.mouse_move(1027, 521)
    ahk.click(1090, 521)
    time.sleep(2) # wait for shop ui

    # buy gears
    buy_gears_idk_2nd()
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
    time.sleep(2)
    ahk.key_press('e')
    time.sleep(2) # wait for seeds ui

def main_loop():
    print('runningggggg')
    time.sleep(5)
    while True:
        main_iteration()
        time.sleep(150)


def test():
    def _dummi():
        ahk.key_press('shift')
        ahk.key_down('s')
        time.sleep(17)
        ahk.key_up('s')
        ahk.key_press('shift')
        time.sleep(2)

    _dummi()
    key_hold('w', 0.2)
    key_hold('d', 1.23)
    time.sleep(1)
    key_hold('d', 0.2)
    time.sleep(1)
    key_hold('d', 0.2)
    time.sleep(1)





# -------------------------------wddd

# MAIN CODE OMAG 


hotkey = '-'
print(f'REMEMBER TO HAVE GEARS SHOP SETUP.\n'*4)
print(f'ready. Press "{hotkey}" to run.')

keyboard.add_hotkey(hotkey, main_loop)
keyboard.wait()
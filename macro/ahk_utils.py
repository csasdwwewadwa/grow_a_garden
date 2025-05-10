from ahk import AHK
import time

ahk = AHK()
ahk.set_coord_mode('Mouse', 'Screen')


def click_wait(x, y=None, wait=0.3):
    if type(x) == 'tuple':
        x, y = x
    ahk.click(x, y)
    time.sleep(wait)

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
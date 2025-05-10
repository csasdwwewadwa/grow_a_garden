import argparse
import json
import logging
import os
import time
import requests
import logging
import threading

import eel
from eel import chrome, edge
import eel.browsers
import webview
import webview.window

# from . import config, dialogs, packaging, utils
import utils


#### GLOBAL VARIABLES

window = None




def wait_for_server(url, timeout=5):
    start = time.time()
    while time.time() - start < timeout:
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return True
        except:
            pass
        time.sleep(0.2)
    return False




# Setup eels root folder
eel.init('web_ui')

def __can_use_chrome():
    """Identify if Chrome is available for Eel to use"""
    chrome_instance_path = chrome.find_path()
    return chrome_instance_path is not None and os.path.exists(chrome_instance_path)


def __can_use_edge():
    """Identify if Edge is available for Eel to use"""
    return edge.find_path()

@eel.expose
def get_data():
    """Get data"""
    with open(r'data/data.json') as f:
        return json.load(f)
    
@eel.expose
def close_app():
    global window
    if window:
        window.destroy()
    os._exit(0)

@eel.expose
def minimize_app():
    webview.windows[0].minimize()

@eel.expose
def drag_window():
    print('erm im suppopsed to drag the windo ;-;')
    

def start():
    """Start the UI using Eel"""

    global window
    try:
        host = 'localhost'
        port = utils.get_port()
        url = f'http://{host}:{port}/index.html'

        print(f'Server starting at port {port}')
        print('Please do not close this terminal while using auto-py-to-exe - the process will end when the window is closed')

        
        def threadthing():
            eel.start('index.html', mode=None, host=host, port=port, block=True)
            logging.basicConfig(level=logging.DEBUG)
        thread = threading.Thread(target=threadthing)
        thread.start()

        if not wait_for_server(url, timeout=10):  # Increase timeout if needed
            print("Error: Eel server did not start in time.")
            return
        
        window = webview.create_window(
            title='csamacro',
            url=url,
            width=621,
            height=486,
            resizable=False,
            frameless=True,
            background_color='#2C313C'
        )
        webview.start(gui='edgechromium', debug=True)
        

    except (SystemExit, KeyboardInterrupt):
        pass  # This is what the bottle server raises



if __name__ == '__main__':
    start()
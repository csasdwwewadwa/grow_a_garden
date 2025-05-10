import pygetwindow as gw

def getWindowsWithTitle(title):
    windows = []
    for window in gw.getAllWindows():
        if window.title == title:
            windows.append(window)
    return windows

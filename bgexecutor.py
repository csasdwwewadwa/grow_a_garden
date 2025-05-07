import time
import pywinauto
from pywinauto.application import Application
from pywinauto.findwindows import ElementNotFoundError
from pywinauto.keyboard import send_keys # For sending keyboard shortcuts if needed

# --- Configuration ---
# Option 1: Start a new instance of Notepad
app_executable = "notepad.exe"
window_title = "Untitled - Notepad" # Default title for a new Notepad window
# Option 2: Connect to an already running Notepad instance (if you prefer)
# window_title_regex = ".*Notepad" # Use a regex if the title might vary slightly

try:
    # --- Connect to or Start the Application ---

    # Start a new instance (use this typically)
    print(f"Starting {app_executable}...")
    # Using backend='uia' is generally recommended for modern apps, 'win32' for older ones.
    app = Application(backend="uia").start(app_executable)
    print("Waiting for window...")
    # Wait for the main window to appear and be ready
    main_window = app.window(title=window_title)
    main_window.wait('visible ready', timeout=20) # Wait up to 20 seconds
    print(f"Found window: '{main_window.window_text()}'")

    # # --- OR --- Connect to an existing instance (uncomment if needed)
    # print(f"Connecting to existing window matching title regex: '{window_title_regex}'...")
    # app = Application(backend="uia").connect(title_re=window_title_regex)
    # main_window = app.top_window() # Get the main window
    # main_window.wait('visible ready', timeout=10)
    # print(f"Connected to window: '{main_window.window_text()}'")


    # --- Interact with Controls ---

    # 1. Find the main text area (Edit control)
    #    We can often find it by its class name or control type.
    #    Use print_control_identifiers() to explore if unsure.
    #    main_window.print_control_identifiers() # Uncomment this to see control details
    print("Finding text editor...")
    edit_control = main_window.child_window(class_name="Edit")
    edit_control.wait('visible ready') # Ensure the control is ready

    # 2. Type text into the Edit control
    #    .type_keys() simulates typing keystrokes.
    #    It respects modifiers like Shift (+) , Ctrl (^), Alt (%)
    #    Use with_spaces=True to handle spaces correctly.
    #    Use with_newlines=True for Enter key simulation within text.
    print("Typing text...")
    text_to_type = "Hello from pywinauto!\nThis text was typed without moving the mouse.\nLine 3 {ENTER}"
    edit_control.type_keys(text_to_type, with_spaces=True, with_newlines=True, pause=0.05)
    time.sleep(1) # Pause briefly

    # Add special keys example
    edit_control.type_keys("^{END}") # Go to end of document (Ctrl+End)
    edit_control.type_keys("{ENTER}Typing special keys: {TAB} worked!")
    time.sleep(1)

    # 3. Click a menu item (e.g., File menu)
    #    Menus are often accessible directly by name.
    print("Clicking 'File' menu...")
    # This uses accessibility features - it doesn't move the mouse pointer
    main_window.menu_select("File")
    time.sleep(1) # Pause to see the menu open

    # 4. Select a submenu item (e.g., File -> Exit)
    #    Use -> separator for submenus
    #    NOTE: This will close Notepad if uncommented!
    # print("Selecting 'File -> Exit'...")
    # main_window.menu_select("File->Exit")
    # # Handle potential "Save changes?" dialog if needed here
    # # try:
    # #     app.SaveAs.DontSave.click() # Example for Win10 Notepad
    # # except Exception:
    # #     pass

    # Example: Close the File menu by sending ESC key to the window
    print("Sending ESC to close menu...")
    main_window.type_keys("{ESC}") # Send Escape key
    time.sleep(1)

    # Example: Clicking a button if one existed (hypothetical)
    # try:
    #     save_button = main_window.child_window(title="Save", control_type="Button")
    #     save_button.wait('visible ready enabled')
    #     print("Clicking hypothetical 'Save' button...")
    #     save_button.click() # Sends a click message/event, doesn't move cursor
    # except ElementNotFoundError:
    #     print("Hypothetical 'Save' button not found.")

    print("Automation finished successfully.")

except ElementNotFoundError:
    print(f"Error: Could not find a required window or control.")
    print("Make sure the application is running and the titles/controls match.")
    print("Try uncommenting 'print_control_identifiers()' to debug.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Optional: Close the application gracefully if you started it
    # Make sure not to close it if you only connected to an existing one
    # and don't want it closed.
    # if 'app' in locals() and app_executable: # Only close if we started it
    #    try:
    #        print("Closing Notepad...")
    #        main_window.close() # Ask nicely first
    #        # Handle potential save dialog again if necessary
    #    except Exception as close_err:
    #        print(f"Error trying to close gracefully: {close_err}")
    #        # Force kill if needed (use with caution)
    #        # app.kill()
    pass # Keep Notepad open for inspection in this example
import pygetwindow as gw
import time

def find_exact_roblox_window():
    """
    Finds the first visible window with the exact title "Roblox".
    Returns the window object or None if not found.
    """
    target_title = "Roblox"
    print(f"Searching for a visible window with the exact title '{target_title}'...")

    try:
        windows = gw.getWindowsWithTitle(target_title)

        # Filter for exact title match and visibility
        exact_match_windows = [win for win in windows if win.title == target_title and win.visible]

        if not exact_match_windows:
            print(f"No visible window found with the exact title '{target_title}'.")
            return None
        else:
            # Return the first found exact match
            roblox_window = exact_match_windows[0]
            print(f"Found window: '{roblox_window.title}'")
            return roblox_window

    except ImportError:
        print("\nError: The 'pygetwindow' library is not installed.")
        print("Please install it using: pip install pygetwindow")
        return None
    except Exception as e:
        print(f"\nAn unexpected error occurred during window search: {e}")
        return None

def resize_and_move_window(window_obj, x, y, width, height):
    """
    Resizes and repositions a given window object.

    Args:
        window_obj: The pygetwindow Window object.
        x (int): The target x-coordinate (left edge).
        y (int): The target y-coordinate (top edge).
        width (int): The target width.
        height (int): The target height.
    """
    if window_obj is None:
        print("Cannot resize/move: Window object is None.")
        return

    print(f"Attempting to set window to position ({x}, {y}) and size ({width}x{height})...")

    try:
        # Ensure the window is not minimized or maximized before resizing/moving
        if window_obj.isMinimized or window_obj.isMaximized:
             print("  Restoring window state...")
             window_obj.restore()
             # Add a small delay to allow the OS to process the restore
             time.sleep(0.1)

        # Set the position (top-left corner)
        window_obj.topleft = (x, y)

        # Set the size
        window_obj.size = (width, height)

        print("Window resized and moved successfully.")

        # Optional: Bring the window to the front
        window_obj.activate()

    except gw.PyGetWindowException as e:
        print(f"Error manipulating window: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during window manipulation: {e}")


# --- Main execution ---
if __name__ == "__main__":
    # Define your desired dimensions and position here
    target_x = 100
    target_y = 100
    target_width = 800
    target_height = 600

    # --- Step 1: Find the window ---
    roblox_window = find_exact_roblox_window()

    # --- Step 2: If found, print current details and then resize/move ---
    if roblox_window:
        print("\n--- Current Window Details ---")
        # Check if box is available (might be None if minimized etc., though restore() helps)
        if roblox_window.box is not None:
             print(f"  Position (Top-Left): ({roblox_window.left}, {roblox_window.top})")
             print(f"  Dimensions (Width x Height): {roblox_window.width} x {roblox_window.height}")
        else:
             # If box is None, try getting values directly after restore
             print(f"  Position (Top-Left): ({roblox_window.left}, {roblox_window.top})")
             print(f"  Dimensions (Width x Height): {roblox_window.width} x {roblox_window.height}")


        # --- Step 3: Resize and Move the window ---
        #resize_and_move_window(roblox_window, target_x, target_y, target_width, target_height)

        # Optional: You could re-find or check the properties again after a delay
        # to confirm the change, but the function should report success/failure.

    else:
        print("\nWindow manipulation skipped because the target window was not found.")

    input('Press Enter to exit...')
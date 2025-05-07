import eel
import time

# Initialize Eel with the 'web' folder as the root for web files
# The first argument points to the directory where your HTML, CSS, JS files are located.
eel.init('web_ui')

# Define a Python function that can be called from JavaScript
# Use the @eel.expose decorator to make it accessible
@eel.expose
def say_hello_py(name):
    print(f"Hello from Python, {name}!")
    # You can return data back to the JavaScript call
    return f"Python received '{name}' and says hello!"

# Define another Python function, maybe simulating a task
@eel.expose
def perform_task(duration):
    print(f"Python starting task for {duration} seconds...")
    time.sleep(duration) # Simulate work
    print("Python task finished.")
    # You can also call JavaScript functions from Python
    eel.update_status("Python task completed!") # Call a JS function named 'update_status'

eel.start('index.html', size=(700, 500), mode='edge') # Try Edge first, change if needed
// web/script.js

// Function to update the output area with messages
function updateOutput(message) {
    const outputDiv = document.getElementById('outputArea');
    if (outputDiv) {
        outputDiv.textContent = message;
    }
}

// Function to update the status span
function updateStatus(message) {
    const statusSpan = document.getElementById('statusOutput');
    if (statusSpan) {
        statusSpan.textContent = message;
    }
}

// Expose the updateStatus function to Python
eel.expose(updateStatus);


// Wait for the DOM to be fully loaded before adding event listeners
document.addEventListener('DOMContentLoaded', function() {

    const callPythonButton = document.getElementById('callPythonButton');
    const startTaskButton = document.getElementById('startTaskButton');

    // --- Button 1: Call Python and get a return value ---
    if (callPythonButton) {
        callPythonButton.addEventListener('click', async () => {
            console.log("Button clicked: Calling Python say_hello_py...");
            updateOutput("Calling Python..."); // Give immediate feedback

            try {
                // Call the exposed Python function
                // eel.python_function_name(arg1, arg2, ...)(callback_function);
                // The callback function receives the return value from Python
                const response = await eel.say_hello_py("User from JavaScript")();
                console.log("Received response from Python:", response);
                updateOutput("Response from Python:\n" + response); // Display the response
            } catch (error) {
                console.error("Error calling Python function:", error);
                updateOutput("Error calling Python function: " + error);
            }
        });
    } else {
        console.error("Button with ID 'callPythonButton' not found!");
    }

    // --- Button 2: Call Python to start a task ---
     if (startTaskButton) {
        startTaskButton.addEventListener('click', async () => {
            console.log("Button clicked: Calling Python perform_task...");
            updateStatus("Task starting..."); // Give immediate feedback

            try {
                // Call the exposed Python function without expecting a direct return value
                // We expect Python to call back via updateStatus
                await eel.perform_task(3)(); // Pass duration, await completion if needed, but response is via callback

                 // Note: We don't update status here based on the return,
                 // as Python calls updateStatus directly when done.
                 // If perform_task had returned something, we could capture it here.

            } catch (error) {
                console.error("Error calling Python task function:", error);
                updateStatus("Error starting task: " + error);
            }
        });
    } else {
        console.error("Button with ID 'startTaskButton' not found!");
    }


});

console.log("script.js loaded and running.");
// Get initialisation data from the server and setup the ui
window.addEventListener('load', async () => {
  // Get initialisation data from Python
  console.log('Getting data');
  const data = await eel.get_data()();
  console.log('Received data');

  // If the server stops, close the UI
  window.eel._websocket.addEventListener('close', (e) => {
    window.close()
    eel.close_app()
  });
});

// Top bar buttons
document.addEventListener('DOMContentLoaded', () => {
  const controlButtonClose = document.querySelector(".control-button-close");
  controlButtonClose.addEventListener('click', () => {
    window.close();
    eel.close_app();
  });

  const controlButtonMinimize = document.querySelector(".control-button.control-button-minimize")
  controlButtonMinimize.addEventListener("click", () => {
    eel.minimize_app();
  });

  const topBar = document.querySelector(".top-bar")
  topBar.addEventListener("mousedown", (e) => {
    // Only initiate drag with left mouse button
    if (e.button === 0) {
      eel.drag_window();
    }
  });
});
from pynput.keyboard import Controller, Listener, Key
import time

keyboard = Controller()
text_to_spam = "ok "  # Message to spam
stop_spamming = False  # Flag to stop loop
i = 0  # Counter for messages sent

# Function to stop the loop when ESC is pressed
def on_press(key):
    global stop_spamming
    if key == Key.esc:
        stop_spamming = True
        return False  # Stops listener

# Give time to switch to the text input field
time.sleep(5)

# Start key listener
listener = Listener(on_press=on_press)
listener.start()

# Start spamming
while not stop_spamming:
    i += 1  # Increment counter
    keyboard.type(f"{text_to_spam}")  # Adds number before message
    time.sleep(0.5)  # Adjust speed

print(f"Spamming stopped after {i} messages!")

# Import Libraries
from pyrogram import Client
from datetime import datetime
from time import sleep

# Define API ID and API HASH
API_ID = 12345678
API_HASH = "your api hash"

# Create a Client
app =  Client("my_account", API_ID, API_HASH)

# Define a Function to Display Time in the Bio
def DisplayTime():
    # Get Current Time
    current_time =  datetime.now().time().strftime("%H:%M")
    # Start the app
    app.start()
    # Update Bio
    app.update_profile(bio=f"Current Time: {current_time}")
    # Stop the app
    app.stop()
    sleep(10)

while True:
    DisplayTime()



import datetime
import time
import os

def set_alarm():
    alarm_time = input("Set alarm time (HH:MM:SS, 24-hour format): ")
    print(f"Alarm set for {alarm_time}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up! ⏰")
            # Optional: Play sound (Windows only)
            try:
                os.system("start alarm.mp3")  # Replace with your sound file
            except:
                print("Couldn't play sound.")
            break
        time.sleep(1)

set_alarm()

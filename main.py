import pyautogui
import time

MOVE_DISTANCE = 50


def is_cursor_at_edge():
    screen_width, screen_height = pyautogui.size()
    x, y = pyautogui.position()
    return x == 0 or y == 0 or x == screen_width - 1 or y == screen_height - 1


def move_cursor():
    screen_width, screen_height = pyautogui.size()
    x, y = pyautogui.position()

    new_x = (
        x + MOVE_DISTANCE if x + MOVE_DISTANCE < screen_width - 1 else x - MOVE_DISTANCE
    )
    new_y = (
        y + MOVE_DISTANCE
        if y + MOVE_DISTANCE < screen_height - 1
        else y - MOVE_DISTANCE
    )

    pyautogui.moveTo(new_x, new_y, duration=0.5)


def start_prevent_sleep(interval):
    try:
        while True:
            time.sleep(interval)  # Wait for the given interval (in seconds)

            if is_cursor_at_edge():
                print("Cursor at the edge. Stopping the script.")
                break

            move_cursor()
            print("Cursor moved.")

    except KeyboardInterrupt:
        print("Script stopped manually.")


if __name__ == "__main__":
    try:
        minutes = float(input("Enter the time interval in minutes: "))
        interval = minutes * 60  # Convert minutes to seconds
        start_prevent_sleep(interval)
    except ValueError:
        print("Invalid input! Please enter a numeric value for the time interval.")

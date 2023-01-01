import pyautogui
import time
import keyboard

def main():
    num_clicks = 300

    while True:
        #  if the user has press the 'x' key, start auto-click
        if keyboard.is_pressed('x'):
            for i in range(num_clicks):
                pyautogui.click()
        
        # if the user has press the 'q' key, stop auto-click
        if keyboard.is_pressed('q'):
            break

if __name__ == '__main__':
    main()

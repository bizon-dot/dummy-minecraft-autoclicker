import keyboard
import pyautogui,time
import keyboard 

while True:  
        if keyboard.is_pressed('x'):   
            for i in range(300):
                pyautogui.click()
            
        if keyboard.is_pressed('q'):  
                break
   
import pyautogui
import time
import PIL

for i in range(3):
    pyautogui.moveTo(100,100,duration =0.25)
    pyautogui.moveTo(200,100,duration =0.25)
    pyautogui.moveTo(200,200,duration =0.25)
    pyautogui.moveTo(100,200,duration =0.25)
pyautogui(pyautogui.position())
pyautogui.locateCenterOnScreen('findthis.png')


# found = pyautogui.locateCenterOnScreen('findthis.png')
# if(found):
#     pyautogui.moveTo(found.x,found.y,duration = 0.25)
# else:
#     print("Could not find!")

# exit = False
# while not exit:
#     input("Exit?")
#     exit = True
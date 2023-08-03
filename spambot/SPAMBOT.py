import pyautogui, time
time.sleep(5)
f = open("Your text name", "r")
for word in f:
    pyautogui.typrwerite(word)
    pyautogui.press("enter")

import pyautogui, time
time.sleep(5)
f = open("beatles", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
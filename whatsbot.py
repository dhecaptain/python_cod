import pyautogui
import time

# Open WhatsApp
pyautogui.press('win')
time.sleep(1)
pyautogui.write('WhatsApp')
time.sleep(1)
pyautogui.press('enter')
time.sleep(5)

# Select contact
pyautogui.write('Contact Name')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

# Send message
pyautogui.write('Hello, this is my Python code:')
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

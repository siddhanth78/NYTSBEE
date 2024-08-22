import pyautogui
import time

print('open nyt spelling bee')
print('typing will begin in 3 sec')

time.sleep(3)

words = open('out.txt', 'r').readlines()
sorted_words = sorted(words, key=len)

for sw in sorted_words[::-1]:
    pyautogui.typewrite(sw)
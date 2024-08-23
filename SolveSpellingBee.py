import pyautogui
import time

print('open nyt spelling bee')
print('typing will begin in 5 sec')

time.sleep(5)

words = open('out.txt', 'r').readlines()
words[-1] = words[-1]+'\n'
sorted_words = sorted(words, key=len)

for sw in sorted_words:
    pyautogui.typewrite(sw)
    time.sleep(1)

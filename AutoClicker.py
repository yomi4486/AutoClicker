from re import X
from tkinter import Y
import pyautogui
import time

#自作連打ツール（CUI、MADE BY YOMI4486）
#回数
X = 512
#クリック間隔(秒)
Y = 0.001
#処理にかかる時間
print('処理にかかる時間は約',X * Y,'秒です(理論値はそうだけど実際はもっとかかる)')
for num in range (4,-1,-1):
    print(num,'...')
    time.sleep(1)

print('連打！')    

for i in range(X):
    pyautogui.click()
    time.sleep(Y)

print('終了！') 


exit
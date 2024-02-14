#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from datetime import datetime
import random

# exe 파일로 만들기
win = Tk()                               # 창 생성

win.geometry("550x150")                 # 창 크기 확인
win.title("aim_game")                        # 창 이름
win.option_add("*font","맑은고딕 20")    # 폰트 옵션 추가

# 라벨
lab = Label(win)
lab.config(text = '표적개수')
lab.grid(column = 0,row = 0, padx = 20 ,pady = 20)

# 엔트리
ent = Entry(win)
ent.grid(column = 1,row = 0, padx = 20 ,pady = 20)

k = 1
def cc():
    global k
    if k < num_t: 
        k +=1
        btn.destroy()
        ran_btn()
    else:
        fin = datetime.now()
        dif_sec = (fin - start).total_seconds()
        btn.destroy()
        lab = Label(win)
        lab.config(text = 'Clear'+str(dif_sec)+'초')
        lab.pack(pady=230)
        

def ran_btn():
    global btn
    btn = Button(win)
    btn.config(bg = 'red')
    btn.config(command = cc)
    btn.config(text = k)
    btn.place(relx = random.random(),rely = random.random())
    
def btn_f():
    global num_t
    global start
    num_t = int(ent.get())
    for wg in win.grid_slaves(): 
        wg.destroy()
    win.geometry("500x500")
    ran_btn()
    start = datetime.now()
# 버튼
btn = Button(win)
btn.config(text = '시작')
btn.config(command = btn_f)
btn.grid(column = 0, row = 1, columnspan=2)

win.mainloop()                           # 창 실행


# In[ ]:





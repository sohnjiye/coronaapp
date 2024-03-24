from tkinter import *
from urllib import request
from bs4 import BeautifulSoup
import time
import tkinter as tk

target = request.urlopen("http://ncov.mohw.go.kr/")
soup = BeautifulSoup(target, "html.parser")

name = []
num = []

for item in soup.select("div.rpsam_graph"):
    for data in item.select("span.name"):
        name.append(str(data.string))

for item in soup.select("div.rpsam_graph"):
    for data in item.select("span.before"):
        data.str=''.join(filter(str.isalnum, data.string))
        num.append(str(data.str))

dic = dict(zip(name,num))

def pressed():
    label.configure(text="버튼을 누름")

def corona():
    global in_text
    global area

    area = input_text.get()
    in_text = "  " + input_text.get()+"의 코로나 확진자 현황 : +" + dic[area]

    if area in dic:
        a = int(dic[area])
        if a <= 10:
            img1 = PhotoImage(file="img (2).gif")
            canvas.create_image(300, 300, image=img1)
            label.configure(text=in_text)
            window.geometry('450x250')
            tk.mainloop()

        elif a <= 50:
            img2 = PhotoImage(file="img (1).gif")
            canvas.create_image(300, 300, image=img2)
            label.configure(text=in_text)
            window.geometry('450x250')
            tk.mainloop()

        else:
            img3 = PhotoImage(file="img.gif")
            canvas.create_image(300,300,image=img3)
            label.configure(text=in_text)
            window.geometry('450x250')
            tk.mainloop()


window = Tk()
tk = tk.Toplevel()
tk.title("캔버스")

window.title("3조 프로젝트")
window.geometry('560x300')

canvas = Canvas(tk, width=600,height=600,bg="white")
canvas.pack()

label = Label(window, text= " "+"지역명을 입력해주세요. ex)서울, 인천, 경기", font=("돋음", 20))
label.grid(column=0, row=0)

date = Label(window, text=time.strftime('%y-%m-%d %H:%M:%S'),font=('돋움',10))
date.grid(column=0,row=1)

input_text = Entry(window, width=30)
input_text.grid(column=0, row=2)

button = Button(window, text="확인", command=corona,width=10,height=3)
button.grid(column=0, row=3)

window.mainloop()

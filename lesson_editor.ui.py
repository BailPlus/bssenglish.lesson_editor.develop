from tkinter import *

def add():
    row = len(word_entry_lst)
    wordent = Entry(f2);wordent.grid(row=row,column=0)
    pronent = Entry(f2);pronent.grid(row=row,column=1)
    tranent = Entry(f2);tranent.grid(row=row,column=2)
    word_entry_lst.append((wordent,pronent,tranent))

root = Tk()
root.title('课程文件编辑器')
f = Frame(root);f.pack()
Label(f,text='当前文件：a.blf').grid(row=0,column=0)
Button(f,text='打开').grid(row=0,column=1)
Button(f,text='保存').grid(row=0,column=2)
word_entry_lst = []
f2 = Frame(root);f2.pack()
Button(root,text='+',command=add).pack()
root.mainloop()

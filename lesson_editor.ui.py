from tkinter import *

def add(*_):
    row = len(word_entry_lst)
    wordent = Entry(f2);wordent.grid(row=row,column=0)
    pronent = Entry(f2);pronent.grid(row=row,column=1)
    tranent = Entry(f2);tranent.grid(row=row,column=2)
    delbtn = Button(f2,text='-');delbtn.grid(row=row,column=3)
    tup = (wordent,pronent,tranent,delbtn)
    delbtn.config(command=lambda:delete(tup))
    word_entry_lst.append(tup)
def delete(tup:tuple):
    for i in tup:
        i.grid_forget()
    word_entry_lst.remove(tup)

root = Tk()
root.title('课程文件编辑器')
root.bind('<Return>',add)
f = Frame(root);f.pack()
Label(f,text='当前文件：a.blf').grid(row=0,column=0)
Button(f,text='打开').grid(row=0,column=1)
Button(f,text='保存').grid(row=0,column=2)
word_entry_lst = []
f2 = Frame(root);f2.pack()
Button(root,text='+',command=add).pack()
root.mainloop()

from tkinter import *
root = Tk()
root.title('课程文件编辑器')
f = Frame(root);f.pack()
Label(f,text='当前文件：a.blf').grid(row=0,column=0)
Button(f,text='打开').grid(row=0,column=1)
Button(f,text='保存').grid(row=0,column=2)
f2 = Frame(root);f2.pack()
for i in range(5):
    for j in range(3):
        Entry(f2).grid(row=i,column=j)
Button(root,text='+').pack()
root.mainloop()

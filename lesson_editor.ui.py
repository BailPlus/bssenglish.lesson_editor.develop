from tkinter import *
import libfile

def add(*_):
    row = len(word_entry_lst)
    wordent = Entry(f2);wordent.grid(row=row,column=0)
    pronent = Entry(f2);pronent.grid(row=row,column=1)
    tranent = Entry(f2);tranent.grid(row=row,column=2)
    delbtn = Button(f2,text='-');delbtn.grid(row=row,column=3)
    c.yview_moveto(1)
    tup = (wordent,pronent,tranent,delbtn)
    delbtn.config(command=lambda:delete(tup))
    word_entry_lst.append(tup)
def delete(tup:tuple):
    for i in tup:
        i.grid_forget()
    word_entry_lst.remove(tup)

word_entry_lst = []

#配置界面
root = Tk()
root.title('课程文件编辑器')
root.bind('<Return>',add)
f0 = Frame(root);f0.pack()   # 界面第一行
Label(f0,text='当前文件：a.blf').grid(row=0,column=0)
Button(f0,text='打开').grid(row=0,column=1)
Button(f0,text='保存').grid(row=0,column=2)
f1 = Frame(root);f1.pack()  # 课程基本信息
Label(f1,text='简称').grid(row=1,column=0)
name_entry = Entry(f1)
name_entry.grid(row=1,column=1)
Label(f1,text='全称').grid(row=2,column=0)
fullname_entry = Entry(f1)
fullname_entry.grid(row=2,column=1)
Label(f1,text='作者').grid(row=3,column=0)
auchor_entry = Entry(f1)
auchor_entry.grid(row=3,column=1)
# 中间主体
c = Canvas(root)
c.pack(fill=BOTH,expand=True)
f2 = Frame(c)
f2.pack()
c.create_window(0,0,window=f2)
bar = Scrollbar(c,orient=VERTICAL,command=c.yview)
bar.pack(side=RIGHT,fill=Y)
c.config(yscrollcommand=bar.set)
f2.bind_all('<Configure>',lambda _:c.config(scrollregion=c.bbox(ALL)))
'''鼠标滚轮适配参考文献:
https://www.codenong.com/17355902'''
c.bind_all('<Button-4>',lambda _:c.yview_scroll(-1,UNITS))  # linux鼠标上键
c.bind_all('<Button-5>',lambda _:c.yview_scroll(1,UNITS))   # linux鼠标下键
c.bind_all('<MouseWheel>',lambda e:c.yview_scroll(1,UNITS) if e.delta<0 else c.yview_scroll(-1,UNITS))  #windows/mac鼠标滚轮

Button(root,text='+',command=add).pack(side=BOTTOM)
root.mainloop()

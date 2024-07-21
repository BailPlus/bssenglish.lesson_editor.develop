from tkinter import *
from tkinter import filedialog
import libfile

def add(*_):
    '''添加单词条目'''
    row = len(word_entry_lst)
    wordent = Entry(words_frame);wordent.grid(row=row,column=0)
    pronent = Entry(words_frame);pronent.grid(row=row,column=1)
    tranent = Entry(words_frame);tranent.grid(row=row,column=2)
    delbtn = Button(words_frame,text='-');delbtn.grid(row=row,column=3)
    c.yview_moveto(1)   # 滚动到底部
    tup = (wordent,pronent,tranent,delbtn)
    delbtn.config(command=lambda:delete(tup))
    word_entry_lst.append(tup)
def delete(tup:tuple):
    '''删除单词条目
tup(tuple):包含单词条目所有控件的元组'''
    for i in tup:
        i.grid_forget()
    word_entry_lst.remove(tup)
def openfile():
    global filename
    filename = filedialog.askopenfilename(parent=root,title='打开')
    lesson = libfile.readfile(filename)
    filename_label.config(text=f'当前文件：{filename}')
    name_entry.delete(0,END)
    name_entry.insert(0,lesson.name)
    fullname_entry.delete(0,END)
    fullname_entry.insert(0,lesson.fullname)
    auchor_entry.delete(0,END)
    auchor_entry.insert(0,lesson.author)
    

word_entry_lst = [] # 所有单词条目
filename:str = None

#配置界面
root = Tk()
root.title('课程文件编辑器')
root.bind('<Return>',add)
filename_frame = Frame(root);filename_frame.pack()   # 界面第一行
filename_label = Label(filename_frame,text=f'当前文件：{filename}')
filename_label.grid(row=0,column=0)
Button(filename_frame,text='打开',command=openfile).grid(row=0,column=1)
Button(filename_frame,text='保存').grid(row=0,column=2)
lessoninfo_frame = Frame(root);lessoninfo_frame.pack()  # 课程基本信息
Label(lessoninfo_frame,text='简称').grid(row=1,column=0)
name_entry = Entry(lessoninfo_frame)
name_entry.grid(row=1,column=1)
Label(lessoninfo_frame,text='全称').grid(row=2,column=0)
fullname_entry = Entry(lessoninfo_frame)
fullname_entry.grid(row=2,column=1)
Label(lessoninfo_frame,text='作者').grid(row=3,column=0)
auchor_entry = Entry(lessoninfo_frame)
auchor_entry.grid(row=3,column=1)
c = Canvas(root)    # 中间主体
c.pack(fill=BOTH,expand=True)
words_frame = Frame(c)
words_frame.pack()
c.create_window(0,0,window=words_frame)
bar = Scrollbar(c,orient=VERTICAL,command=c.yview)
bar.pack(side=RIGHT,fill=Y)
c.config(yscrollcommand=bar.set)
words_frame.bind_all('<Configure>',lambda _:c.config(scrollregion=c.bbox(ALL)))
'''鼠标滚轮适配参考文献:
https://www.codenong.com/17355902'''
c.bind_all('<Button-4>',lambda _:c.yview_scroll(-1,UNITS))  # linux鼠标上键
c.bind_all('<Button-5>',lambda _:c.yview_scroll(1,UNITS))   # linux鼠标下键
c.bind_all('<MouseWheel>',lambda e:c.yview_scroll(1,UNITS) if e.delta<0 else c.yview_scroll(-1,UNITS))  #windows/mac鼠标滚轮

Button(root,text='+',command=add).pack(side=BOTTOM)
root.mainloop()

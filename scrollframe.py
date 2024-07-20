#滚动框架实现方案研究
from tkinter import *
root =Tk()
c = Canvas(root)
c.pack(fill=BOTH,expand=True)
f = LabelFrame(c,bg='#ff0000')
f.pack()#side=LEFT,fill=BOTH,expand=True)
c.create_window((0,0),window=f)
s = Scrollbar(c,orient=VERTICAL,command=c.yview)
s.pack(side=RIGHT,fill=Y)
c.config(yscrollcommand=s.set)
f.bind('<Configure>',lambda _:c.config(scrollregion=c.bbox(ALL)))
c.bind('<MouseWheel>',lambda e:c.yview(SCROLL,e.delta,UNITS))

for i in range(200):
    Button(f,command=lambda:c.yview_moveto(1)).pack()

root.mainloop()

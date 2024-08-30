from tkinter import*
from random import*
w=Tk()
w[&#39;bg&#39;]=&quot;white&quot;
w.title(&quot;otp generator&quot;)
w.geometry(&quot;600x600&quot;)
def screenclear():
e1.delete(0,END)
def function():
    screenclear()
    l=[]
    g="";
    for i in range(6):
        l.append(randint(0,9))
    for i in l:
        g=g+str(i)
    e1.insert(0,g)
e1=Entry(w,width=90,font=(&quot;ArialBlack&quot;,50),fg=&quot;silver&quot;,bg=&quot;maroon&quot;,justif
y=CENTER)
e1.pack(expand=True)
b=Button(w,text=&quot;click here to generate the
otp&quot;,width=20,font=(&quot;Arial&quot;,20),padx=20,pady=20,fg=&quot;white&quot;,bg=&quot;maroon&quot;,ba
ckground=&quot;black&quot;,command=function)
b.pack(expand=True)
w.mainloop()
from tkinter import *
import pyshorteners


def urlfunc():
    url_enter= copiedurl.get()
    output = pyshorteners.Shortener().tinyurl.short(url_enter)
    url_short.insert(END,output)

def clear_text():
    copiedurl.delete(0,END)
    url_short.delete(0,END)

window=Tk()
window.title('URL Shortner Application')
window.configure(background="#8D9D3B")
#window.iconbitmap("callogo.ico")
window.geometry("550x260")
window.resizable(width=False, height=False)
img = PhotoImage(file="abc.png",height=90,width=115)
#Label(window,image=img)

Label(window,image=img,border=False).pack(side=TOP)
Label(window, text="Generate Short URL", font=("Times new roman", 20, "bold"),bg="black", fg="Red").pack(side=TOP)


orignal_url_frame = Frame(window)
Label(orignal_url_frame, text="Paste URL").pack(side=LEFT)
copiedurl= Entry(orignal_url_frame,width=52,font=("Arial 12"))
copiedurl.pack()
orignal_url_frame.pack(pady=10)



short_url_frame = Frame(window)
Label(short_url_frame, text="Short URL").pack(side=LEFT)
url_short= Entry(short_url_frame,width=52,font=("Arial 12"))
url_short.pack()
short_url_frame.pack(pady=10)

Button(window,text="Link",command=urlfunc).pack(side = LEFT, expand = True, fill = BOTH)
Button(window,text="Clear",command=clear_text).pack(side = LEFT, expand = True, fill = BOTH)
window.mainloop()
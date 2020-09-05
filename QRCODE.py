import qrcode
from tkinter import *
from tkinter import messagebox
root = Tk()
def reset():
    web_entry.delete(0,END)
    web_entry.config(bg='white')
    QR.config(image='',text='',width=20,height=20)

def qr_code():
    global fileName
    web_site = web_entry.get()
    try:
        web = web_site.split('.')
        if web_site.startswith('www.'):
            if web_site.endswith('.com'):
                fileName = web[1]+'.jpg'
        else:
            fileName = web[0]+'.jpg'
    except:
        fileName = web_site
# generate and save qrcode

    if len(web_site) < 1:
        messagebox.showerror('Waring','Enter your information first...')
        web_entry.config(bg='red2')
        QR.config(text='there is error occured in generating QR code',fg='red',font=('times new roman',10,'bold'))
    else:
        img = qrcode.make(web_site)
        img.save(fileName)
        root.photo = PhotoImage(file=fileName)
        QR.config(image=root.photo,text='QR code generated successfully!',fg='green',compound=TOP,width=300,height=300)



#==========GUI Detailed ========
root.title('QR code generator')
root.config(bg='light blue')
root.geometry('540x550+350+100')
root.resizable(False,False)
#root.iconbitmap()
head_lbl = Label(root,text='QR CODE GENERATOR',bg='light blue',fg='blue'
                ,font=('forte',25,'underline'))
head_lbl.place(x=80,y=10)
website = Label(root,text='Enter Your Information:',font=('impact',15)
                 ,fg='black',bg='light blue')

website.place(x=10,y=70)
web_entry = Entry(root,fg='blue',font=('times new roman',15),bd=10,width=30)
web_entry.place(x=210,y=70)

getQR_code = Button(root,text="GET QR CODE",fg='red',bg='black'
                    ,font=('Goudy new style',15),width=20,activeforeground='yellow',
                    command=qr_code)
getQR_code.place(x=170,y=130)

reset_app = Button(root,text="RESET",bg='grey',fg='black',width=15,bd=6,command=reset)
reset_app.place(x=400,y=500)

QR = Label(root,image='',bg='light blue')
QR.place(x=130,y=190)

root.mainloop()










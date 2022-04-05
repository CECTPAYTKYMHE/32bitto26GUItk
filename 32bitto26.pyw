import tkinter as tk
import webbrowser
def card32to26():
    id = data32.get()
    id = int(id)
    card32 = (bin(id))[-24:]
    card26l = card32[-12:]
    card26f = card32[:-12]
    if card26f.count('1') % 2 == 1:
        card26f = '1' + card26f
    if card26l.count('1') % 2 == 0:
        card26l += '1'
    else:
        card26l += '0'
    card26 = card26f + card26l
    card26 = int(card26,2)
    data26.delete(0,'end')
    data26.insert(0,card26)
    data32.delete(0,'end')

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

root = tk.Tk()
root.title('Преобразование карты из Wiegand32 в Wiegand26')
root.geometry('270x150+700+300')
root.resizable(False,False)
tk.Label(root, text='32 bit: ').grid(row=0,column=0,stick='w')
data32 = tk.Entry(root)
data32.grid(row=0,column=1,stick='w')
tk.Label(root, text='26 bit: ').grid(row=1,column=0,stick='w')
data26 = tk.Entry(root)
data26.grid(row=1,column=1,stick='w')

btn1 = tk.Button(root, text='Преобразовать',
                command=card32to26).grid(row=2,column=1,stick='w')

tk.Label(root, text='Разработка: ДИТ СКФУ').grid(row=3,column=1,stick='w')
lbl = tk.Label(root, text=r"https://github.com/CECTPAYTKYMHE", fg="blue", cursor="hand2")
lbl.grid(row=4,column=1,stick='w')
lbl.bind("<Button-1>", callback)


root.mainloop()






        





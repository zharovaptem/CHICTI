from tkinter import *

def start_function():
    global img_btn_gray, img_btn_red, img_btn_yellow, img_btn_green, btn_start, btn_pause, btn_stop, label_status_bar
    label_status_work = Label(text="Статус работы:", font=("Inner", 26))
    label_status_work.place(x=210,y=20)
    label_status_bar = Label(text="Выключен", font=("Inner", 26), fg="red")
    label_status_bar.place(x=460, y=20)

    canvas.create_rectangle(100, 70, 300, 270, fill="#B7B7B7")
    canvas.create_rectangle(350, 70, 550, 270, fill="#B7B7B7")
    canvas.create_rectangle(600, 70, 800, 270, fill="#B7B7B7")

    img_btn_gray = PhotoImage(file="flud/gray.png")
    img_btn_red = PhotoImage(file="red.png")
    img_btn_yellow = PhotoImage(file="yellow.png")
    img_btn_green = PhotoImage(file="flud/green.png")

    btn_start = canvas.create_image(199, 165, image=img_btn_gray)
    canvas.tag_bind(btn_start, "<Button-1>", lambda event: machine_start())

    btn_pause = canvas.create_image(449, 165, image=img_btn_gray)
    canvas.tag_bind(btn_pause, "<Button-1>", lambda event: machine_pause())

    btn_stop = canvas.create_image(699, 165, image=img_btn_gray)
    canvas.tag_bind(btn_stop, "<Button-1>", lambda event: machine_stop())

def machine_start():
    if (label_status_bar.cget("text") == "Выключен"):
        canvas.itemconfig(btn_start, image=img_btn_green)
        canvas.itemconfig(btn_pause, image=img_btn_gray)
        canvas.itemconfig(btn_stop, image=img_btn_gray)
        label_status_bar.configure(text="Работает", fg="green")

def machine_pause():
    if (label_status_bar.cget("text") == "Работает"):
        canvas.itemconfig(btn_pause, image=img_btn_yellow)
        label_status_bar.configure(text="Остановлен", fg="yellow")
    elif (label_status_bar.cget("text") == "Остановлен"):
        canvas.itemconfig(btn_pause, image=img_btn_gray)
        label_status_bar.configure(text="Работает", fg="green")

def machine_stop():
    global after_func
    label_status_bar.configure(text="Выключен", fg="red")
    canvas.itemconfig(btn_start, image=img_btn_gray)
    canvas.itemconfig(btn_pause, image=img_btn_gray)
    canvas.itemconfig(btn_stop, image=img_btn_red)
    after_func = canvas.after(1500, lambda: canvas.itemconfig(btn_stop, image=img_btn_gray))

root = Tk()
root.title("Кнопки")
root.geometry("900x300")
root.resizable(False, False)
canvas = Canvas(width=900, height=300, bg="#EDEDED")
canvas.place(x=0, y=0)
start_function()

root.mainloop()
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import get_data, qr_code

def authorisation():
    login = login_entry.get()
    password = pass_entry.get()
    # login = "login11"
    # password = "pass11"
    if login and password:
        data = get_data.auth(login, password)
        if data:
            global type
            type = data[3]
            if (type == "Заказчик"):
                zakazchik_window()
            elif (type == "Мастер"):
                print(2)
            elif (type == "Оператор"):
                print(3)
            elif (type == "Менеджер"):
                print(4)
        else:
            messagebox.showerror("Ошибка!", "Неверный логин или пароль!")
    else:
        messagebox.showerror("Ошибка!", "Неверный логин или пароль!")


def close():
    window.destroy()
    main_frame()


def zakazchik_window():
    global window
    window = Tk()
    window.title("Заказчик")
    window.geometry("700x500")
    window.resizable(width=False, height=False)
    back_button = Button(window, text="Назад", font=("Inter", 20), command=lambda: close())
    back_button.place(x=590, y=20)
    qr_button = Button(window, text="Оценить", font=("Inter", 20), command=lambda: qrcode_window())
    qr_button.place(x=20, y=20)
    root.destroy()

def qrcode_window():
    qr_window = Tk()
    qr_window.title("QRCode")
    qr_window.geometry("310x310")
    qr_window.resizable(width=False, height=False)
    canvas = Canvas()
    canvas.place(x=0, y=0)
    qr_image = ImageTk.PhotoImage(file="qr_code.png")
    label = Label(canvas, image=qr_image)
    label.img = qr_image
    label.place(x=30, y=30)


def main_frame():
    global root, login_entry, pass_entry
    root = Tk()
    root.title("Main")
    root.geometry("550x300")
    root.resizable(width=False, height=False)

    login_label = Label(text="Логин", fg="black", font=("Inter", 20))
    login_label.place(x=70, y=50)
    pass_label = Label(text="Пароль", fg="black", font=("Inter", 20))
    pass_label.place(x=70, y=130)

    login_entry = Entry(font=("Inter", 20))
    login_entry.place(x=170, y=50)
    pass_entry = Entry(font=("Inter", 20))
    pass_entry.place(x=170, y=130)

    enter_button = Button(text="Войти", font=("Inter", 20), command=lambda: authorisation())
    enter_button.place(x=250, y=200)

    root.mainloop()


main_frame()
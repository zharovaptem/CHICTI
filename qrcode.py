from tkinter import *
import qrcode

root = Tk()
root.title("")
root.resizable(False, False)
root.geometry("300x400")
canvas = Canvas(width=300, height=400)
canvas.place(x=0, y=0)

data = "https://docs.google.com/forms/d/e/1FAIpQLSdhZcExx6LSIXxk0ub55mSu-WIh23WYdGG9HY5EZhLDo7P8eA/viewform?usp=sf_link"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=6,
    border=2,
)

# Добавление данных в QR-код
qr.add_data(data)
qr.make(fit=True)

# Создание изображения QR-кода в памяти
qr_img = qr.make_image(fill_color="black", back_color="white")

# Преобразование изображения PIL в формат, подходящий для Tkinter
img = PhotoImage(canvas, image=qr_img)
label = Label(canvas, image=img)
label.image = img
label.place(x=30,y=30)
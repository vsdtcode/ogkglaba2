import tkinter as tk
from tkinter import Canvas
import re 
from PIL import Image
from datetime import datetime
from functools import partial



#Допоміжні функції
def save_as_png(canvas : Canvas):
    file_name = f"{datetime.now().hour + datetime.now().minute + datetime.now().second}_user_canvas.ps"
    png_file_name = file_name[:len(file_name) - 3]
    canvas.postscript(file = file_name)
    image = Image.open(file_name)
    image.save(f"{png_file_name}.png", "png")

def save_as_jpeg(canvas : Canvas):
    file_name = f"{datetime.now().hour + datetime.now().minute + datetime.now().second}_user_canvas.ps"
    jpeg_file_name = file_name[:len(file_name) - 3]
    canvas.postscript(file = file_name)
    image = Image.open(file_name)
    image.save(f"{jpeg_file_name}.jpeg", "jpeg")

def save_as_tiff(canvas : Canvas):
    file_name = f"{datetime.now().hour + datetime.now().minute + datetime.now().second}_user_canvas.ps"
    tiff_file_name = file_name[:len(file_name) - 3]
    canvas.postscript(file = file_name)
    image = Image.open(file_name)
    image.save(f"{tiff_file_name}.tiff", "tiff")

def save_as_bmp(canvas : Canvas):
    file_name = f"{datetime.now().hour + datetime.now().minute + datetime.now().second}_user_canvas.ps"
    bmp_file_name = file_name[:len(file_name) - 3]
    canvas.postscript(file = file_name)
    image = Image.open(file_name)
    image.save(f"{bmp_file_name}.bmp", "bmp")

def save_as_gif(canvas : Canvas):
    file_name = f"{datetime.now().hour + datetime.now().minute + datetime.now().second}_user_canvas.ps"
    gif_file_name = file_name[:len(file_name) - 3]
    canvas.postscript(file = file_name)
    image = Image.open(file_name)
    image.save(f"{gif_file_name}.gif", "gif")

#Зчитування даних з файлу
dataset = open("DS5.txt", "r", encoding = "utf-8")
    
points = []
for i in dataset:
    line = dataset.readline()
    line = line.lstrip()
    line = line.rstrip()
    
    pattern1 = re.compile(r"\d+\s+")
    pattern2 = re.compile(r"\s+\d+")
    
    x_list = pattern1.findall(line)
    y_list = pattern2.findall(line)

    if (len(x_list) and len(y_list)) != 0:
        points.append((float(x_list[0].rstrip()),float(y_list[0].lstrip())))
        
dataset.close()

#Ініціалізація вікна
window = tk.Tk()
window.title("Відображення точок з датасету. ФПМ КМ-33 Страшний Василь")
window.geometry("960x540")

#Ініціалізація полотна 
canvas = tk.Canvas(window,width = 960, height = 540, bg = "white")
canvas.pack()


#Експорт у JPEG, PNG та інші формати
menu_bar = tk.Menu(window)
export_menu = tk.Menu(menu_bar, tearoff = 0)
export_menu.add_command(label = "PNG", command = partial(save_as_png,canvas))
export_menu.add_command(label = "JPEG", command = partial(save_as_jpeg,canvas))
export_menu.add_command(label = "TIFF", command = partial(save_as_tiff,canvas))
export_menu.add_command(label = "BMP", command = partial(save_as_bmp,canvas))
export_menu.add_command(label = "GIF", command = partial(save_as_gif,canvas))
menu_bar.add_cascade(label = "Експорт", menu = export_menu)
window.config(menu = menu_bar)

#Відображення точок у полотні 
for p in points:
    canvas.create_oval(p[0], 540 - p[1], p[0] + 3, 540 - p[1] - 3, fill = "black")

window.mainloop()

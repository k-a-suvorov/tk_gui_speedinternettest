# This is my first program for working with network
# pip install speedtest-cli mostly required
# pip install pandas mostly required too

try:
    import speedtest
    from tkinter import *
    from tkinter import Tk
    import csv
    import pandas as pd
    import time
    import os.path

except ImportError:
    print('Ошибка в загрузке модулей!')

def change_log():
    # Изменения в программе

    delete_text()
    result = f'Убраны эксперементальные и забагованные функции.\n' \
             f'В текстовое поле добавлен скроллбар.\n' \
             f'Добавлены обработчики ошибок.\n' \
             f'Добавлена описательная статистика с помощью pandas.describe()\n' \
             f'Исправлены некоторые ошибки форматированного вывода текста.' \


    text.insert(1.0, result)


def stat_info():
        # Небольшая описательная Статистика

    delete_text()
    dataframe = pd.read_csv('speedtest.csv')
    print(text.insert(1.0, dataframe.describe()))

#    return text.insert(1.0, dataframe)


def version_info():
    # Версия программы
    return 'Created by K. Suvorov, ver: 0.3'


def about():
    # Окно версии программы

    a = Toplevel()
    a.geometry('240x160')
    a.title('О программе')
    a['bg'] = 'white'
    a.overrideredirect(True)
    Label(a, text=version_info()).pack(expand=1)
    a.after(5000, lambda: a.destroy())


def insert_text():
    # Вставить текст

    s = speedTest()
    text.insert(1.0, s)


def delete_text():
    # Удалить текст

    text.delete(1.0, END)


def speedTest():
    # Определение скрости Интернет Загрузка /Отдача

    test = speedtest.Speedtest()
    download = test.download() / 1048576
    upload = test.upload() / 1048576
    cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())


    if os.path.isfile('speedtest.csv'):
        with open('speedtest.csv', mode='a', encoding='utf=8') as w_file:
            file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
            file_writer.writerow([cur_time, download, upload])
    else:
        with open('speedtest.csv', mode='w', encoding='utf=8') as w_file:
            file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
            file_writer.writerow(["Time", "DownloadSpeed - Mb/s", "UploadSpeed - Mb/s"])
            file_writer.writerow([cur_time, download, upload])

    return f"Speed: {round(download, 2)} Mb/s \n Upload Speed : {round(upload)} Mb/s"


root: Tk = Tk()

# Размеры окна

WIDTH = 620
HEIGHT = 320

# Вычисление координат окна

POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

# Установление ширины и высоты окна

root.geometry(F'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')

root.title('SpeedNetwork Tools')
root.resizable(False, False)

# Текст и скроллбар

text = Text(root, width=100, height=12)
scroll = Scrollbar(command=text.yview)
scroll.pack(side=RIGHT, fill=Y)

text.config(yscrollcommand=scroll.set)
text.pack()

# Работа с Frame()

frame = Frame()
frame.pack()
Button(frame, text="О программе",
       command=about).pack(side=LEFT)
Button(frame, text="Скорость интернета",
       command=insert_text).pack(side=LEFT)
Button(frame, text="Статистика",
       command=stat_info).pack(side=LEFT)
Button(frame, text="ChangeLog",
       command=change_log).pack(side=LEFT)
Button(frame, text="Quit", command=root.destroy).pack(side=LEFT)


try:
    root.mainloop()
except EXCEPTION:
    print('Ошибка в значениях или типах данных, или неизвестная ошибка!')

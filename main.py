# Итоговая аттестация

# GUI-приложение «Random Password Generator» ("Генератор случайных паролей")

# Импорт необходимых библиотек
import tkinter as tk
from tkinter import ttk
import random
import string
import json
from datetime import datetime


def generate_password():
    pass

# Главное окно
root = tk.Tk()
root.title("Генератор случайных паролей")
root.geometry("700x900")
root.configure(bg="#b8e9b6")

# Переменная длины пароля
length_pasw = tk.IntVar(value=4)  # начальное значение 4 (для сверхпростого пароля)

# Переменные для чекбоксов
lowercase_var = tk.BooleanVar(value=True) # по умолчанию один из блоков включен изначально, чтобы избежать ошибки генерации
uppercase_var = tk.BooleanVar(value=False)
digits_var = tk.BooleanVar(value=False)
special_var = tk.BooleanVar(value=False)

# Метка приветствия
label_intro = tk.Label(root, text="Добро пожаловать в программу генерации надежных паролей!",  font=("Arial", 16, "bold"), bg="#b8e9b6", wraplength=450)
label_intro.pack(pady=10)

# Метка-инструкция для пользователя
label_1 = tk.Label(root, text="Выберите нужные компоненты пароля:", font=("Arial", 12, "bold"), bg="#b8e9b6")
label_1.pack(pady=10)

# Чекбоксы
tk.Checkbutton(root, text="строчные буквы (a-z)", variable=lowercase_var).pack(padx=50, pady=3, anchor="w")
tk.Checkbutton(root, text="ЗАГЛАВНЫЕ БУКВЫ (A-Z)", variable=uppercase_var).pack(padx=50, pady=3, anchor="w")
tk.Checkbutton(root, text="Цифры (0-9)", variable=digits_var).pack(padx=50, pady=3, anchor="w")
tk.Checkbutton(root, text="Спецсимволы", variable=special_var).pack(padx=50, pady=3, anchor="w")

# Метка для отображения текущей длины
label_scale = tk.Label(root, text="Выберите желаемую длину пароля (4-64):", font=("Arial", 12, "bold"), bg="#b8e9b6")
label_scale.pack(pady=10)

# Ползунок длины пароля
pasword_length_scale = tk.Scale(root, from_=4, to=64, length=590, orient=tk.HORIZONTAL, variable=length_pasw)
pasword_length_scale.pack(pady=5, padx=20)

# Кнопка генерации
button_pasw = tk.Button(root, text='Сгенерировать пароль!', font=("Arial", 12, "bold"), fg='red', command=generate_password)
button_pasw.pack(pady=20)

root.mainloop()


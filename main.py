# Итоговая аттестация

# GUI-приложение «Random Password Generator» ("Генератор случайных паролей")

# Импорт необходимых библиотек
import tkinter as tk
from tkinter import ttk
import random
import string
import json
from datetime import datetime

# Загрузка сохраненных паролей
def load_passwords_list():
    try:
        with open("password_generator.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Сохранение истории генераций
def save_password_list(passw_list):
    try:
        with open("password_generator.json", "w", encoding="utf-8") as file:
            json.dump(passw_list, file, ensure_ascii=False, indent=4)
            print("Задачи успешно сохранены в password_generator.json")
    except PermissionError:
        print("Нет прав на запись файла password_generator.json. Проверьте права доступа к директории.")
    except FileNotFoundError:
        print("Файл password_generator.json не найден. Будет создан новый.")
    except TypeError as e:
        print(f"Неподдерживаемый тип данных в задачах: {e}")
    except OSError as e:
        print(f"Ошибка файловой системы: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

# Генерация и отображения паролей
def generate_password():
    # Получаем длину пароля из переменной, привязанной к ползунку
    length = length_pasw.get()
    
    # Формируем набор символов на основе чекбоксов
    all_chars = (
        (string.ascii_lowercase if lowercase_var.get() else '') +
        (string.ascii_uppercase if uppercase_var.get() else '') +
        (string.digits if digits_var.get() else '') +
        ("!@#$%^&*()_+-={}|;:,.<>?" if special_var.get() else '') )
    
    # Проверяем, что хотя бы один тип символов выбран
    if not all_chars:
        result_label.config(text="Ошибка: выберите хотя бы один тип символов!", fg="red")
        return
    
    # Генерируем пароль и время его создания
    password = ''.join(random.choices(all_chars, k=length))
    current_time = datetime.now().strftime("%H:%M:%S")
    passwords.append({'password': password, 'timestamp': current_time, 'length': len(password)})

    # Отображаем и сохраняем результат в файл
    result_label.config(text=f"Сгенерированный пароль:\n {password}", fg="blue")   
    save_password_list(passw_list=passwords)
    update_history_listbox() # Обновляем историю в Listbox

# Обновляет историю в Listbox
def update_history_listbox():
    # Очистка Listbox
    lb.delete(0, tk.END)
    if not passwords:
        lb.insert(tk.END, "История пуста")
    else:
        for password in passwords:
            line = f"Пароль: {password['password']} ({password['length']} симв.) — {password['timestamp']}"
            lb.insert(tk.END, line)

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

# Метка для результата
result_label = tk.Label(root, text=" ", font=("Arial", 12, "bold"), bg="#b8e9b6")
result_label.pack(pady=5)

# Метка для истории генераций
result_history = tk.Label(root, text="История генераций:", font=("Arial", 12, "bold"), bg="#b8e9b6")
result_history.pack(pady=5)

# Фрейм для истории с скроллбаром
frame = tk.Frame(root, bg="#90d6f7")
frame.pack(padx=40, pady=20, fill='both', expand=True)

# Listbox для истории
lb = tk.Listbox(frame, height=10, width=40, bg='#90d6f7', fg="#030303", selectmode=tk.SINGLE, font=("Arial", 8))
lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Скроллбар
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Связываем скроллбар и Listbox
lb.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lb.yview)

# Загружаем в историю генераций
passwords = load_passwords_list()

root.mainloop()

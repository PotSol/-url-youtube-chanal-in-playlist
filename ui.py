import re
import tkinter as tk
from tkinter import ttk

def is_valid_channel_id(channel_id):
    """Проверка корректности идентификатора канала."""
    return re.match(r'UC[^\s/]+', channel_id) is not None

def convert_channel_to_playlist():
    """Преобразование идентификатора канала в URL плейлиста."""
    channel_id = url_entry.get()
    if is_valid_channel_id(channel_id):
        playlist_url = f"https://www.youtube.com/playlist?list=UU{channel_id[2:]}"
        result_label.config(text=f"URL плейлиста: {playlist_url}")
        copy_button.config(state=tk.NORMAL)  # Активируем кнопку копирования
    else:
        result_label.config(text="Некорректный идентификатор канала")
        copy_button.config(state=tk.DISABLED)  # Деактивируем кнопку копирования

def copy_to_clipboard():
    """Копирование URL плейлиста в буфер обмена."""
    playlist_url = result_label.cget("text").split("URL плейлиста: ")[-1]
    root.clipboard_clear()
    root.clipboard_append(playlist_url)

def paste_from_clipboard():
    """Вставка идентификатора канала из буфера обмена."""
    clipboard_content = root.clipboard_get()
    if is_valid_channel_id(clipboard_content):
        url_entry.delete(0, tk.END)
        url_entry.insert(0, clipboard_content)

# Создание главного окна
root = tk.Tk()
root.title("Конвертер идентификатора канала YouTube в URL плейлиста")

# Добавление метки и поля ввода для идентификатора канала
ttk.Label(root, text="Введите идентификатор канала:").grid(row=0, column=0, padx=10, pady=10)
url_entry = ttk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Добавление кнопки для вставки из буфера обмена
paste_button = ttk.Button(root, text="Вставить", command=paste_from_clipboard)
paste_button.grid(row=0, column=2, padx=10, pady=10)

# Добавление кнопки для выполнения конвертации
convert_button = ttk.Button(root, text="Конвертировать", command=convert_channel_to_playlist)
convert_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Добавление метки для отображения результата
result_label = ttk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Добавление кнопки для копирования URL
copy_button = ttk.Button(root, text="Копировать", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Запуск главного цикла приложения
root.mainloop()

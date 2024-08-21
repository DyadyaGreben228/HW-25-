#import requests
#import json
#import os
#
#def fetch_data(post_id):
#    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
#    response = requests.get(url)
#    
#    if response.status_code == 200:
#        data = response.json()
#        print("Data fetched successfully.")
#        return data
#    else:
#        print("Failed to fetch data.")
#        return None
#
#def save_data(post_id, data):
#    if data:
#        os.makedirs("json_data", exist_ok=True)
#        file_path = f"json_data/post_{post_id}.json"
#        with open(file_path, 'w') as file:
#            json.dump(data, file, indent=4)
#        print(f"Data saved to {file_path}")
#    else:
#        print("No data to save.")
#
## Пример использования
#post_id = 1  # Задайте нужный ID
#data = fetch_data(post_id)
#save_data(post_id, data)










import requests
import json
import os
import tkinter as tk
from tkinter import messagebox

def fetch_data(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        messagebox.showerror("Ошибка", "Не удалось получить данные.")
        return None

def save_data(post_id, data):
    if data:
        os.makedirs("json_data", exist_ok=True)
        file_path = f"json_data/post_{post_id}.json"
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo("Успех", f"Данные сохранены в {file_path}")
    else:
        messagebox.showerror("Ошибка", "Нет данных для сохранения.")

def on_fetch_click():
    post_id = entry_id.get()
    if post_id.isdigit():
        data = fetch_data(int(post_id))
        save_data(int(post_id), data)
    else:
        messagebox.showerror("Ошибка", "Введите корректный ID.")

# Создание графического интерфейса
root = tk.Tk()
root.title("JSONPlaceholder Fetcher")

frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

label_id = tk.Label(frame, text="Введите ID поста:")
label_id.grid(row=0, column=0, padx=5, pady=5)

entry_id = tk.Entry(frame)
entry_id.grid(row=0, column=1, padx=5, pady=5)

btn_fetch = tk.Button(frame, text="Получить данные", command=on_fetch_click)
btn_fetch.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
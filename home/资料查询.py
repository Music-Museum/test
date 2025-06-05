#!/usr/bin/env python3
# coding: UTF-8
import os
import sqlite3
import tkinter as tk
from tkinter import font
from tkinter import messagebox

DB_PATH = os.path.expanduser("~/Desktop/11.db")

root = tk.Tk()
root.title("资料查询")
root.configure(bg="#F0EAD6")
root.resizable(False, False)

my_font = font.Font(family="Helvetica", size=10)

main_frame = tk.Frame(root, bg="#F0EAD6")
main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

search_frame = tk.Frame(main_frame, bg="#F0EAD6")
search_frame.grid(row=0, column=0, sticky="w", padx=7, pady=5)

search_entry = tk.Entry(search_frame, width=25, highlightbackground='#DCD0C0',
                        highlightcolor='#A9A9A9', highlightthickness=1, bd=0)
search_entry.pack(side=tk.LEFT, padx=(0, 5), pady=2)

result_list = tk.Listbox(main_frame, height=5, bg="white", relief="flat",
                         selectbackground="#f2c6b4", width=30)
result_list.grid(row=1, column=0, sticky="ew", padx=7, pady=(0, 5))

def search_csv():
    query = search_entry.get().strip()
    if not query:
        return

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT "物料号", "描述" 
            FROM products 
            WHERE "物料号" LIKE ? OR "描述" LIKE ?
            LIMIT 100
        """, (f"%{query}%", f"%{query}%"))

        result_list.delete(0, tk.END)
        for row in cursor:
            result_list.insert(tk.END, f"{row[0]} {row[1]}")

        conn.close()
    except Exception as e:
        messagebox.showerror("错误", f"数据库查询失败：{str(e)}")

def copy_to_clipboard():
    selected = result_list.get(tk.ACTIVE)
    if selected:
        root.clipboard_clear()
        root.clipboard_append(selected.strip())
        root.update()

def copy_first_result():
    if result_list.size() > 0:
        result_list.selection_clear(0, tk.END)
        result_list.selection_set(0)
        result_list.activate(0)
        copy_to_clipboard()

search_entry.bind("<KeyRelease>", lambda e: root.after(300, search_csv))
search_entry.bind("<Return>", lambda e: copy_first_result())

copy_btn = tk.Button(search_frame, text="复制", command=copy_to_clipboard, font=my_font,
                     bg="#f2c6b4", fg="#696969", activebackground="#C0B090",
                     relief="flat")
copy_btn.pack(side=tk.LEFT, padx=(5, 0))
result_list.bind("<Double-Button-1>", lambda e: copy_to_clipboard())

root.mainloop()

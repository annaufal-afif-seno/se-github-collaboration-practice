import json
import os
from src.task_manager import (
    get_all_tasks,
    add_task,
    update_task_status,
    delete_task,
    search_task_by_assignee
)
 
DATA_FILE = "data/tasks.json"
 
 
def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)
 
 
def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)
 
 
def display_tasks(tasks):
    if not tasks:
        print("Tidak ada task.")
        return
    print(f"\n{'ID':<5} {'Title':<30} {'Status':<15} {'Priority':<10} {'Assignee':<15}")
    print("-" * 80)
    for task in tasks:
        print(f"{task['id']:<5} {task['title']:<30} {task['status']:<15} {task['priority']:<10} {task['assignee']:<15}")
    print()
 
 
def main():
    tasks = load_tasks()
 
    while True:
        print("\n===== TO-DO LIST MANAGER =====")
        print("1. Lihat semua task")
        print("2. Tambah task baru")
        print("3. Update status task")
        print("4. Hapus task")
        print("5. Cari task berdasarkan assignee")
        print("0. Keluar")
 
        choice = input("\nPilih menu: ").strip()
 
        if choice == "1":
            display_tasks(get_all_tasks(tasks))
 
        elif choice == "2":
            title = input("Judul task: ").strip()
            description = input("Deskripsi: ").strip()
            priority = input("Prioritas (high/medium/low): ").strip()
            assignee = input("Assignee: ").strip()
            tasks = add_task(tasks, title, description, priority, assignee)
            save_tasks(tasks)
            print("Task berhasil ditambahkan!")
 
        elif choice == "3":
            display_tasks(tasks)
            task_id = int(input("Masukkan ID task: "))
            new_status = input("Status baru (todo/in_progress/done): ").strip()
            tasks = update_task_status(tasks, task_id, new_status)
            save_tasks(tasks)
            print("Status berhasil diupdate!")
 
        elif choice == "4":
            display_tasks(tasks)
            task_id = int(input("Masukkan ID task yang akan dihapus: "))
            tasks = delete_task(tasks, task_id)
            save_tasks(tasks)
            print("Task berhasil dihapus!")
 
        elif choice == "5":
            keyword = input("Masukkan nama assignee: ").strip()
            results = search_task_by_assignee(tasks, keyword)
            display_tasks(results)
 
        elif choice == "0":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")
 
 
if __name__ == "__main__":
    main()
 
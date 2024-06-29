import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        
        self.task_listbox = tk.Listbox(
            self.frame, height=15, width=50, bd=0, selectmode=tk.SINGLE)
        
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.update_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.complete_button = tk.Button(self.button_frame, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.tasks = []

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append((task, False))
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            new_task = self.task_entry.get()
            if new_task != "":
                _, completed = self.tasks[selected_task_index]
                self.tasks[selected_task_index] = (new_task, completed)
                self.task_listbox.delete(selected_task_index)
                display_text = f"{new_task} (Completed)" if completed else new_task
                self.task_listbox.insert(selected_task_index, display_text)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task, completed = self.tasks[selected_task_index]
            if not completed:
                self.tasks[selected_task_index] = (task, True)
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, f"{task} (Completed)")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def on_closing(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoList(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()



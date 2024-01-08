import tkinter as tk

class DrawMenuWindow(tk.Toplevel):
    def __init__(self, master=None, exit_handler=None):
        super().__init__(master)
        self.master = master
        self.exit_handler = exit_handler
        self.title("Draw Menu Window")
        self.geometry("400x300")
        self.configure(bg="#333333")

        label = tk.Label(self, text="Draw Menu Window", font=("Helvetica", 16), bg="#333333", fg="white")
        label.pack(pady=20)

        back_button = tk.Button(self, text="뒤로 가기", command=self.back_to_main, bg="#555555", fg="white", width=15)
        back_button.pack(pady=10)

    def back_to_main(self):
        self.destroy()
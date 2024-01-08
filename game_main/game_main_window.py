import tkinter as tk

from draw_card.draw_card_window import DrawMenuWindow


class GameMainWindow(tk.Toplevel):
    def __init__(self, master=None, exit_handler=None):
        super().__init__(master)
        self.master = master
        self.exit_handler = exit_handler
        self.title("Game Main Window")
        self.geometry("800x600")
        self.configure(bg="#333333")

        button_frame = tk.Frame(self, bg="#333333")
        button_frame.pack(side="right", padx=20)

        # 뽑기, 덱 구성, 레이드, 배틀, 종료 메뉴 추가
        draw_button = tk.Button(button_frame, text="뽑기", command=self.draw_menu, bg="#555555", fg="white", width=15)
        draw_button.grid(row=0, column=0, pady=10)

        deck_button = tk.Button(button_frame, text="덱 구성", command=self.deck_menu, bg="#555555", fg="white", width=15)
        deck_button.grid(row=1, column=0, pady=10)

        raid_button = tk.Button(button_frame, text="레이드", command=self.raid_menu, bg="#555555", fg="white", width=15)
        raid_button.grid(row=2, column=0, pady=10)

        battle_button = tk.Button(button_frame, text="배틀", command=self.battle_menu, bg="#555555", fg="white", width=15)
        battle_button.grid(row=3, column=0, pady=10)

        exit_button = tk.Button(button_frame, text="종료", command=self.exit_game, bg="#555555", fg="white", width=15)
        exit_button.grid(row=4, column=0, pady=10)


    def draw_menu(self):
        print("뽑기 메뉴를 선택하였습니다.")
        deck_menu_frame = DrawMenuWindow(self, self.back_to_main)
        deck_menu_frame.pack()

    def deck_menu(self):
        print("덱 구성 메뉴를 선택하였습니다.")

    def raid_menu(self):
        print("레이드 메뉴를 선택하였습니다.")

    def battle_menu(self):
        print("배틀 메뉴를 선택하였습니다.")

    def exit_game(self):
        print("프로그램 종료")
        self.master.quit()
        self.exit_handler()


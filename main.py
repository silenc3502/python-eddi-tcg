import tkinter as tk

from game_main.game_main_window import GameMainWindow


def start_game():
    # 게임을 시작하는 함수를 정의할 수 있습니다.
    print("Game started!")
    game_main_window = GameMainWindow(root, exit_game)
    print("is it operate ?")
    root.withdraw()

def exit_game():
    # 게임을 종료하는 함수를 정의할 수 있습니다.
    root.destroy()

# tkinter 윈도우 생성
root = tk.Tk()
root.title("EDDI TCG Card Battle")

# 윈도우 크기 설정
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# 배경색을 어두운 색상으로 설정
root.configure(bg="#333333")

# 프레임을 이용하여 상하 가운데 정렬 설정
frame = tk.Frame(root, bg="#333333")
frame.place(relx=0.5, rely=0.5, anchor="center")

# 레이블을 이용하여 텍스트 표시 (양쪽 정렬)
label_text = "EDDI TCG Card Battle"
label = tk.Label(frame, text=label_text, font=("Helvetica", 16), bg="#333333", fg="white", justify="center")
label.pack(pady=20)

# "Game Start" 버튼
start_button = tk.Button(frame, text="Game Start", command=start_game, bg="#555555", fg="white")
start_button.pack(pady=10, side="left", padx=10)

# "Exit" 버튼
exit_button = tk.Button(frame, text="Exit", command=exit_game, bg="#555555", fg="white")
exit_button.pack(pady=10, side="left", padx=10)

# tkinter 메인 루프 시작
root.mainloop()

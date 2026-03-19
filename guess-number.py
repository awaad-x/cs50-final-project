import customtkinter as ctk
import random
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Guess The Number")
app.geometry("500x600")
app.resizable(False, False)

# Global Variables
number = 0
attempts = 0
max_attempts = 10
max_number = 100
time_left = 30
score = 0
best_score = 0
game_running = False

# Frames
start_frame = ctk.CTkFrame(app)
game_frame = ctk.CTkFrame(app)
start_frame.pack(fill="both", expand=True)

# ---------------- Start Screen ----------------
title = ctk.CTkLabel(start_frame, text="🎯 GUESS THE NUMBER", font=("Arial", 28, "bold"), text_color="#00ffcc")
title.pack(pady=40)

best_score_label = ctk.CTkLabel(start_frame, text=f"Best Score: {best_score}", font=("Arial",18))
best_score_label.pack(pady=10)

difficulty_var = ctk.StringVar(value="Medium")
difficulty_menu = ctk.CTkOptionMenu(start_frame, values=["Easy","Medium","Hard"], variable=difficulty_var, width=200)
difficulty_menu.pack(pady=15)

mode_var = ctk.StringVar(value="Dark")
mode_menu = ctk.CTkOptionMenu(start_frame,
                               values=["Light","Dark","System"],
                               variable=mode_var,
                               width=200,
                               command=lambda m: ctk.set_appearance_mode(m))
mode_menu.pack(pady=10)

developer_label_start = ctk.CTkLabel(start_frame, text="🎯 By Mohamed Awaad", font=("Arial",14,"bold"), text_color="#ffaa00")
developer_label_start.pack(side="bottom", anchor="e", padx=20, pady=10)

# ---------------- Logic ----------------
def set_difficulty(level):
    global max_attempts, max_number
    if level=="Easy": max_attempts,max_number = 15,50
    elif level=="Medium": max_attempts,max_number = 10,100
    else: max_attempts,max_number = 7,200

def back_to_menu():
    global best_score
    game_frame.pack_forget()
    best_score_label.configure(text=f"Best Score: {best_score}")
    start_frame.pack(fill="both", expand=True)

def start_game():
    global number, attempts, time_left, game_running
    number = random.randint(1,max_number)
    attempts = 0
    time_left = 30
    game_running = True

    feedback_label.configure(text="")
    entry_widget.delete(0, ctk.END)
    entry_widget.configure(fg_color="white")
    attempts_label.configure(text=f"Attempts: {max_attempts}")
    timer_label.configure(text=f"Time: {time_left}")

    submit_btn.configure(state="normal")
    entry_widget.configure(state="normal")
    app.after(100, update_timer)
    entry_widget.focus_force()

def update_timer():
    global time_left
    if not game_running: return
    if time_left>0:
        timer_label.configure(text=f"Time: {time_left}")
        time_left-=1
        app.after(1000, update_timer)
    else:
        game_over()

def game_over():
    global game_running
    game_running=False
    messagebox.showinfo("Game Over", f"The number was {number}")
    back_to_menu()

def calculate_score():
    global score, best_score
    score += (max_attempts - attempts)*10
    if score>best_score: best_score = score
    score_label.configure(text=f"Score: {score}")

def shake():
    x=app.winfo_x(); y=app.winfo_y()
    def move(i):
        if i<10:
            offset = 10 if i%2==0 else -10
            app.geometry(f"+{x+offset}+{y}")
            app.after(30, move, i+1)
        else: app.geometry(f"+{x}+{y}")
    move(0)

def flash_entry(color):
    entry_widget.configure(fg_color=color)
    app.after(500, lambda: entry_widget.configure(fg_color="white"))

def check_guess(event=None):
    global attempts, game_running, score, best_score
    if not game_running: return
    try: guess=int(entry_widget.get())
    except ValueError:
        feedback_label.configure(text="Enter valid number!")
        flash_entry("red")
        entry_widget.delete(0, ctk.END)
        return

    attempts += 1
    entry_widget.delete(0, ctk.END)
    attempts_left = max_attempts - attempts
    attempts_label.configure(text=f"Attempts: {attempts_left}")

    if guess>number:
        feedback_label.configure(text="Too high!")
        shake()
        flash_entry("red")
    elif guess<number:
        feedback_label.configure(text="Too low!")
        shake()
        flash_entry("red")
    else:
        game_running=False
        calculate_score()
        flash_entry("green")
        messagebox.showinfo("🎉 You Win!", f"You guessed it in {attempts} attempts!\nScore: {score}")
        back_to_menu()
        return

    if abs(guess-number)<=5 and guess!=number:
        feedback_label.configure(text=feedback_label.cget("text")+" | Very close!")

    if attempts>=max_attempts:
        game_running=False
        messagebox.showinfo("Game Over", f"The number was {number}")
        back_to_menu()

def start_button():
    set_difficulty(difficulty_var.get())
    start_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)
    start_game()

# ---------------- Start Button ----------------
start_btn = ctk.CTkButton(start_frame, text="▶ Start Game", font=("Arial",18,"bold"), width=220, height=50, command=start_button)
start_btn.pack(pady=30)

# ---------------- Game Screen ----------------
container = ctk.CTkFrame(game_frame, corner_radius=20, fg_color="#222222")
container.pack(pady=20, padx=20, fill="both", expand=True)

title2 = ctk.CTkLabel(container, text="🎯 GUESS THE NUMBER", font=("Arial",26,"bold"), text_color="#00ffcc")
title2.pack(pady=15)

info_frame = ctk.CTkFrame(container, fg_color="#333333")
info_frame.pack(pady=10, padx=10, fill="x")

attempts_label = ctk.CTkLabel(info_frame, text=f"Attempts: {max_attempts}", font=("Arial",14))
attempts_label.grid(row=0,column=0,padx=15, pady=5)
timer_label = ctk.CTkLabel(info_frame, text=f"Time: {time_left}", font=("Arial",14))
timer_label.grid(row=0,column=1,padx=15, pady=5)
score_label = ctk.CTkLabel(info_frame, text=f"Score: {score}", font=("Arial",14))
score_label.grid(row=0,column=2,padx=15, pady=5)

entry_widget = ctk.CTkEntry(
    container,
    placeholder_text="Enter a number...",
    font=("Arial",18),
    width=250,
    height=45,
    corner_radius=12,
    text_color="black"
)
entry_widget.pack(pady=20)

feedback_label = ctk.CTkLabel(container, text="", font=("Arial",16,"bold"), text_color="#ffcc00")
feedback_label.pack(pady=10)

btn_frame = ctk.CTkFrame(container, fg_color="transparent")
btn_frame.pack(pady=15)

submit_btn = ctk.CTkButton(btn_frame, text="Submit", font=("Arial",16,"bold"), width=120, height=45, corner_radius=10, command=check_guess)
submit_btn.grid(row=0,column=0,padx=10)
restart_btn = ctk.CTkButton(btn_frame, text="Restart", font=("Arial",16), width=120, height=45, corner_radius=10, command=start_game)
restart_btn.grid(row=0,column=1,padx=10)

developer_label_game = ctk.CTkLabel(container, text="🎯 By Mohamed Awaad", font=("Arial",12,"bold"), text_color="#ffaa00")
developer_label_game.pack(side="bottom", anchor="e", padx=20, pady=5)

app.bind("<Return>", check_guess)
app.mainloop()
import os
import tkinter as tk
from tkinter import ttk
import pygame

# Directory where game files are stored
GAMES_DIRECTORY = "C:\\Users\\sahil\\Desktop\\openx"

# List of available games (modify this list as needed)   
AVAILABLE_GAMES = [
    "Quiz",
    "Eat_the_Fruit",
    "Rock_Paper_Scissors",
    "Guess_The_Number"
]

# Initialize Pygame for playing background music
pygame.mixer.init()

# Function to play background music
def play_background_music():
    pygame.mixer.music.load("BGM.mp3")
    pygame.mixer.music.play(-1)  # Play music indefinitely

# Function to stop background music
def stop_background_music():
    pygame.mixer.music.stop()

# Function to start the selected game
def start_game():
    loading_label.config(text="Loading...")
    loading_label.update()
    
    stop_background_music()  # Stop background music when game starts
    selected_game = game_listbox.get(game_listbox.curselection())
    game_path = os.path.join(GAMES_DIRECTORY, f"{selected_game}.py")
    os.system(f"python {game_path}")
    
    loading_label.config(text="Choose a game")
    play_background_music()

# Create Tkinter window
root = tk.Tk()
root.title("CV Games!!!")
root.geometry("1000x1000")

# Load and set background image
bg_image = tk.PhotoImage(file="back.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Filter available games based on AVAILABLE_GAMES list
game_files = [file[:-3] for file in os.listdir(GAMES_DIRECTORY) if file[:-3] in AVAILABLE_GAMES]

# Create a listbox to display game options
game_listbox = tk.Listbox(root,  font=("Comic Sans MS", 25,"bold"), selectbackground="red",cursor="cross", height=6)
for game in game_files:
    game_listbox.insert(tk.END, game)
game_listbox.place(relx=0.5, rely=0.5, anchor="center")

# Create start game button
start_button = ttk.Button(root, text="Start Game", command=start_game, cursor="cross")
start_button.place(relx=0.5, rely=0.6, anchor="center")

loading_label = tk.Label(root, text="", font=("Comic Sans MS", 12))
loading_label.place(relx=0.5, rely=0.65, anchor="center")

# Start playing background music
play_background_music()

# Run the Tkinter event loop
root.mainloop()

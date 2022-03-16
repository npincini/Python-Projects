import tkinter as tk

# Creation of the window application w/Title
root=tk.Tk()
root.title("Rock/Paper/Scissors @npincini ")
root.geometry("400x400")
root.resizable(0,0) #Can't resize
root['bg']='black'

# Creation and Placement of Title
Title = tk.Label(root, text="Rock/Paper/Scissors:", relief="groove")
Title.place(relx=0.005, rely=0.005, relwidth=0.99, relheight=0.15)


# Keeps the application running
root.mainloop()




# For learning Tkinter: https://tkdocs.com/tutorial/concepts.html
# If you need help: https://github.com/Rajchowdhury420/Rock-paper-scissors-Game/blob/master/game.py

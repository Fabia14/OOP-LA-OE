import tkinter as tk

your_name = "FABIA_JOHNLEONNNE"
sec = "BSIT- 2B"
anime = "AOT"
akin_to = tk.Tk()
akin_to.title(f"OOP")

frame = tk.Frame(akin_to)
frame.pack(pady=20)

label = tk.Label(frame, text=(f"OOP LA30, {your_name} {sec}"))
label.grid(row=0, column=0, padx=100, pady=50)

counter = 0

def display_text():
    global counter
    print(f"{counter} My Favorite anime is {anime}")
    counter += 1

button = tk.Button(akin_to, text="Click Me", command=display_text)
button.pack(pady=10)

akin_to.geometry("500x300")

akin_to.mainloop()
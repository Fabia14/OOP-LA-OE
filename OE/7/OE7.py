import tkinter as tk

your_name = "FABIA_JOHNLEONNE"
sec = "BSIT- 2B"
anime = "AOT"
counter = 0

def display_text():
    global counter
    print(f"{counter} My Favorite anime is {anime}")
    counter += 1

app = tk.Tk()
app.title("OOP")

frame = tk.Frame(app)
frame.pack(pady=20)

label = tk.Label(frame, text=f"OOP LA29, {your_name} {sec}")
label.grid(row=0, column=0, padx=100, pady=50)

button = tk.Button(app, text="DOT MO BEH", command=display_text)
button.pack(pady=10)

app.geometry("500x300")
app.mainloop()
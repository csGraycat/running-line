import tkinter as tk
import time

if __name__ == '__main__':
    start_time = time.time()
    font_size = 50
    var = 'Привет!'
    root = tk.Tk()
    canvas = tk.Canvas(root, bg="black", width=100, height=100)
    canvas.pack(fill=tk.BOTH, expand=1)
    text = canvas.create_text(100, 50, text=var, anchor=tk.W,
                              fill='white', font=("Courier", font_size))

    while time.time() - start_time < 3:
        canvas.update()
        canvas.move(text, -1-(font_size/100)*len(var), 0)
        time.sleep(0.03)

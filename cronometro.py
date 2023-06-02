import time
import tkinter as tk

class cronometro:

    def __init__(self, segundos=0, minutos=0, horas=0):
        self.segundos = segundos
        self.minutos = minutos
        self.horas = horas
    
    def __repr__(self):
        return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}'
    
    def incremento(self):
        self.segundos += 1
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1

def update_time():
    cronometro1.incremento()
    time_label.config(text=str(cronometro1))
    root.after(1000, update_time)

cronometro1 = cronometro()

root = tk.Tk()
root.title("Cronômetro")

time_label = tk.Label(root, text=str(cronometro1), font=("Helvetica", 36))
time_label.pack()

update_time()

root.mainloop()

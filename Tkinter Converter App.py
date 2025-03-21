import tkinter as tk
from tkinter import ttk

def convert():

    #Miles to Kilometers
    if dropdown.get() == 'Miles':
        mil_input = entry_int.get()
        km_output = mil_input *1.61
        output_string.set(km_output)

    #Kilometers to Miles
    if dropdown.get() == 'Kilometers':
        km_input = entry_int.get()
        mil_output = km_input /1.61
        output_string.set(mil_output)
    
    #Inches to Centimeters
    if dropdown.get() == 'Inches':
        inch_input = entry_int.get()
        cm_output = inch_input *2.54
        output_string.set(cm_output)
    
    #Centimeters to Inches
    if dropdown.get() == 'Celcius':
        cel_input = entry_int.get()
        fah_output = cel_input *9/5 +32
        output_string.set(fah_output)
    
    #Celcius to Fahrenheit
    if dropdown.get() == 'Fahrenheit':
        fah_input = entry_int.get()
        cel_output = (fah_input -32) *5/9
        output_string.set(cel_output)
    

#Setup window
window = tk.Tk()
window.title('Converter Apps')
window.geometry('400x150')

#Label judul
title_label = ttk.Label(window, text ='Converter App', font ='Times 26 bold')
title_label.pack()

#Kolom entry/input dan setup button
input_frame = ttk.Frame(window)
dropdown = ttk.Combobox(input_frame, values = ['Miles', 'Kilometers', 'Inches', 'Celcius', 'Fahrenheit'])
dropdown.set('Miles')
dropdown.pack(side ='left')

entry_int = tk.IntVar()
entry = ttk.Entry(input_frame, textvariable = entry_int)
button = ttk.Button(input_frame, text ='Convert',command = convert)
input_frame.pack(pady = 10)
entry.pack(side ='left',padx = 10)
button.pack(side ='left')

#Output label
output_string = tk.StringVar()
output_label = ttk.Label(window, text ='Output', font ='Calibri 26 bold', textvariable = output_string)
output_label.pack(pady=5)

#Run program
window.mainloop()

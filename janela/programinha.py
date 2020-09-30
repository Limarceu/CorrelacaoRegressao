'''Este é um programa complementar a disciplina de análise exploratória.add()'''

'''Este programa serve para resolver exercicios de correlação e regressão linear,
dado um dataset ou um banco de dados.'''

import tkinter as tk


janela = tk.Tk()
janela.title('Correlacao e Regressao')
janela.geometry('300x500')

#função faz algo
def add():
    res_box.delete(1.0, 'end')
    try:
        res_box.insert(tk.INSERT, int(first_nr.get()) + int(second_nr.get())
    except ValueError:
        res_box.insert(tk.TK(INSERT, 'number required')

def sub():
    res_box.delete(1.0, 'end')
    try:
        res_box.insert(tk.INSERT, int(first_nr.get()) - int(second_nr.get()))
    except ValueError:
        res_box.insert(tk.INSERT, 'Number Required')

#all elements inside the window
lbl_nr_one = tk.Label(janela, text='Digite o primeiro numero: ', bg='green')
lbl_nr_one.pack(padx = 5, pady = 5)
lbl_nr_two = tk.Label(janela, text = "Digite o segundo número", bg='red')
lbl_nr_two.pack(padx=10,pady=5)

button_add = tk.Button(janela, text='Numeros Adicao', command = add)
button_add.pack()
button_sub = tk.Button(janela, text = 'subtract numero', command=sub)
button_sub.pack()

lbl_res = tk.Label(janela, text='Resuldado é: ')
lbl_res.pack(padx=10, pady=5)

res_box = tk.Text(janela, width=15, height = 1)
res_box.pack(padx=10, pady=5)

janela.mainloop()

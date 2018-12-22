from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
c=0

def function(x,y):
   #print(taxa)
   eq=taxa*y
   return eq

def calcular():
    h=0.1 
    c =int((s/h)+1)
    x = np.zeros(c)
    y = np.zeros(c)
    x[0]=0
    y[0]=pvi
    print(x[0],y[0])
    for i in np.arange(1,c):
      y[i]=y[i-1]+(function(x[i-1],y[i-1]))*h
      x[i]=x[i-1]+h
      print(x[i],y[i])
    plt.title('Empréstimos Bancários')
    plt.xlabel('Tempo(meses)')
    plt.ylabel('Saldo(reais)')
    plt.plot(x,y)
    plt.show()
    
    
def bt_click():
   z=float(ed.get())
   global pvi
   global taxa
   taxa=z/100
   pvi=int(ed1.get())
   global s
   s=int(ed2.get())
   calcular()

janela = Tk();
ed = Entry(janela)
ed.place(x=110, y=100)
ed1 = Entry(janela)
ed1.place(x=110, y=160)
ed2 = Entry(janela)
ed2.place(x=110, y=220)
lbl=Label(janela, width=50, text= "SIMULADOR EMPRÉSTIMO BANCÁRIO: ")
lbl.place(x=140, y=10)
lb=Label(janela, width=25, text= "TAXA DE JUROS (% AO MÊS) : ")
lb.place(x=98, y=80)
lb1=Label(janela, width=20, text= "VALOR EMPRÉSTIMO (PVI): ")
lb1.place(x=105, y=130)
lb2=Label(janela, width=20, text= "QUANTIDADE DE MESES: ")
lb2.place(x=100, y=190)
bt=Button(janela, width=20, text =" Plotar Gráfico",command= bt_click)
bt.place(x=400,y=150)
janela.title("Capitalizaçao de Juros");
janela.geometry("600x300+100+100")
janela.mainloop()






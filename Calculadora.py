from tkinter import *
equacao=" "

#-------- FUNCOES -------#

def soma(valor):
    global equacao
    equacao += valor
    print(equacao)
    texto_resultado.config(text=equacao)

def calcular():
    global equacao
    resultado = eval(equacao)
    print(resultado)
    texto_resultado.config(text=resultado)
    equacao = str(resultado)
    pass

def limpar():
    global equacao
    equacao=" "
    texto_resultado.config(text=equacao)

# ------- LAYOUT ------- #

janela =Tk()
janela.title("CALCULADORA PYTHON")
altura = 650
largura = 500
janela.resizable(True, True)
janela.configure(bg='white')
alturatela = janela.winfo_screenheight()
larguratela = janela.winfo_screenwidth()
posx = larguratela/2 - largura/2
posy = alturatela/2  - altura/2
janela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
janela.columnconfigure(0,weight=1)

img = PhotoImage(file="Imagem/download.png")
label_imagem = Label(janela,image=img, bg='white')

texto_resultado = Label(janela, text=" ",font=3200, height = 5, width = 10, bg='white')

botao7 = Button(janela,text="  7  ",font=200, height = 5, width = 10, bg="#28348A", fg="white", command=lambda :soma("7"))
botao8 = Button(janela,text="  8  ", font=200, height = 5, width = 10, bg="#28348A", fg="white",command=lambda :soma("8"))
botao9 = Button(janela,text="  9  ", font=200, height = 5, width = 10,bg="#28348A", fg="white", command=lambda :soma("9"))
botaoporcentagem= Button(janela,text="  %  ", font=200, height = 5, width = 11,bg="#28348A", fg="white", command=lambda :soma("%"))
botaoC= Button(janela,text="  C  ", font=200, height = 5, width = 11, bg="#28348A", fg="white",command=lambda :limpar())

botao4 = Button(janela,text="  4  ",font=200, height = 5, width = 10,bg="#28348A", fg="white",command=lambda :soma("4"))
botao5 = Button(janela,text="  5  ", font=200, height = 5, width = 10,bg="#28348A", fg="white",command= lambda :soma("5"))
botao6 = Button(janela,text="  6  ", font=200, height = 5, width = 10,bg="#28348A", fg="white",command=lambda :soma("6"))
botaoMultiplicacao= Button(janela,text="   X  ", font=200, height = 5, width = 11,bg="#28348A", fg="white",command=lambda :soma("*"))
botaoDivisao= Button(janela,text="  /   ", font=200, height = 5, width = 11,bg="#28348A", fg="white",command=lambda :soma("/"))

botao1 = Button(janela,text="  1  ", font=200, height = 5, width = 10,bg="#28348A", fg="white",command=lambda :soma("1"))
botao2 = Button(janela,text="  2  ", font=200, height = 5, width = 10,bg="#28348A", fg="white",command=lambda :soma("2"))
botao3 = Button(janela,text="  3  ", font=200, height = 5, width = 10,bg="#28348A", fg="white",command=lambda :soma("3"))
botaoAdicao= Button(janela,text="    +    ", font=200, height = 5, width = 11,bg="#28348A", fg="white",command=lambda :soma("+"))
botaoSubtracao= Button(janela,text="    -    ", font=200, height = 5, width = 11, bg="#28348A", fg="white",command=lambda :soma("-"))

botaoResultado= Button(janela,text="=", width=34, font=200, height = 5,bg="#28348A", fg="white", command=lambda :calcular())
botaoPonto= Button(janela,text="   .   ", font=200, height = 5, width = 10,bg="#28348A", fg="white",command=lambda :soma("."))
botao0= Button(janela,text="  0  ", font=200, height = 5, width = 10,bg="#28348A", fg="white", command=lambda :soma("0"))

label_imagem.grid(column=0, row=0, columnspan=15)
texto_resultado.grid(column=0, row=1, columnspan=15 )
botao7.grid(column=0,row=2)
botao8.grid(column=1,row=2)
botao9.grid(column=2,row=2)
botaoporcentagem.grid(column=3,row=2)
botaoC.grid(column=4,row=2)
botao4.grid(column=0,row=3)
botao5.grid(column=1,row=3)
botao6.grid(column=2,row=3)
botaoMultiplicacao.grid(column=3,row=3)
botaoDivisao.grid(column=4,row=3)
botao1.grid(column=0,row=4)
botao2.grid(column=1,row=4)
botao3.grid(column=2,row=4)
botaoAdicao.grid(column=3,row=4)
botaoSubtracao.grid(column=4,row=4)
botaoResultado.grid(column=2,row=6, columnspan=4)
botaoPonto.grid(column=1,row=6)
botao0.grid(column=0,row=6)


janela.mainloop()
'''
    Done by: Matheus Leal
    Github: https://github.com/MatheusLealAquino
    Year: 2016
'''

from Tkinter import *
class Janela:
    def __init__(self,top):

        self.frame0 = Frame(top)
        self.frame0.pack()

        self.frame1 = Frame(top)
        self.frame1.pack()

        self.frame2 = Frame(top)
        self.frame2.pack()
        
        self.frame3 = Frame(top)
        self.frame3.pack()
        
        self.frame4 = Frame(top)
        self.frame4.pack()

        self.frame5 = Frame(top)
        self.frame5.pack()

        self.frame6 = Frame(top)
        self.frame6.pack()

        self.menu = Label(self.frame0,text = '',font = 'Arial')
        self.menu.pack(side=LEFT)

        self.menu1 = Label(self.frame0,text=' ',font='Arial')
        self.menu1.pack(side=RIGHT)

        self.b0 = Button(self.frame4,text='0',width = 7,command=self.clique0)
        self.b0.pack(side=LEFT)

        self.vir = Button(self.frame4,text ='.',width = 7,command = self.cliquevir)
        self.vir.pack(side = RIGHT)
        
        self.b1 = Button(self.frame3,text='1',width = 7,command=self.clique1)
        self.b1.pack(side=LEFT)

        self.b2 = Button(self.frame3,text='2',width = 7,command=self.clique2)
        self.b2.pack(side=LEFT)

        self.b3 = Button(self.frame3,text='3',width = 7,command=self.clique3)
        self.b3.pack(side=LEFT)
        
        self.b4 = Button(self.frame2,text='4',width = 7,command=self.clique4)
        self.b4.pack(side=LEFT)
        
        self.b5 = Button(self.frame2,text='5',width = 7,command=self.clique5)
        self.b5.pack(side=LEFT)
        
        self.b6 = Button(self.frame2,text='6',width = 7,command=self.clique6)
        self.b6.pack(side=LEFT)

        self.b7 = Button(self.frame1,text='7',width = 7,command=self.clique7)
        self.b7.pack(side=LEFT)

        self.b8 = Button(self.frame1,text='8',width = 7,command=self.clique8)
        self.b8.pack(side=LEFT)

        self.b9 = Button(self.frame1,text='9',width = 7,command=self.clique9)
        self.b9.pack(side=LEFT)

        self.div1 = Label(self.frame5,text = '')
        self.div1.pack()

        self.mais = Button(self.frame5,text='+',width = 7,command=self.acao1)
        self.mais.pack(side=RIGHT)

        self.menos = Button(self.frame5,text='-',width=7,command=self.acao2)
        self.menos.pack(side=RIGHT)

        self.multi = Button(self.frame5,text='X',width = 7,command=self.acao3)
        self.multi.pack(side=RIGHT)

        self.div = Button(self.frame5,text='/',width = 7,command=self.acao4)
        self.div.pack(side=RIGHT)

        self.div2 = Label(self.frame6,text = '')
        self.div2.pack()

        self.resul = Button(self.frame6,text='Resultado',width = 7,command = self.resultado)
        self.resul.pack(side=RIGHT)

        self.clear = Button(self.frame6,text='Limpar',width = 7,command = self.clear)
        self.clear.pack(side=LEFT)

    def clique0(self):
        self.menu['text'] += '0'
        
    def clique1(self):
        self.menu['text'] += '1'

    def clique2(self):
        self.menu['text'] += '2'

    def clique3(self):
        self.menu['text'] += '3'

    def clique4(self):
        self.menu['text'] += '4'

    def clique5(self):
        self.menu['text'] += '5'

    def clique6(self):
        self.menu['text'] += '6'

    def clique7(self):
        self.menu['text'] += '7'

    def clique8(self):
        self.menu['text'] += '8'

    def clique9(self):
        self.menu['text'] += '9'

    def cliquevir(self):
        self.menu['text'] += '.'

    def acao1(self):
        self.menu['text'] += ' + '

    def acao2(self):
        self.menu['text'] += ' - '
        
    def acao3(self):
        self.menu['text'] += ' x '
        
    def acao4(self):
        self.menu['text'] += ' / '

    def resultado(self):
        resul = ''
        numeros = self.menu['text']
        
        lista = numeros.strip().split()
        
        total = float(lista[0])
        
        for i in range(len(lista)):
                if lista[i] == '+':
                    total += float(lista[i+1])
                        
                if lista[i] == '-':
                    total -= float(lista[i+1])

                if lista[i] == 'x':
                    total *= float(lista[i+1])

                if lista[i] == '/':
                    total /= float(lista[i+1])

        self.menu1['text']= '= ' + str(total)
        
    def clear(self):
        self.menu['text'] = ''
        self.menu1['text'] = ''
        
raiz = Tk()
raiz.title('Calculadora - 1.0 (Matheus Leal)')
Janela(raiz)
raiz.mainloop()

from tkinter import *
import tkinter as tk
#criando a janela
root=Tk()
#funções extras
#cpf
def format_cpf(event=None):
    text = ent3.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace": return

    for index in range(len(text)):

        if not text[index] in "0123456789": continue
        if index in [2, 5]:
            new_text += text[index] + "."
        elif index == 8:
            new_text += text[index] + "-"
        else:
            new_text += text[index]

    ent3.delete(0, "end")
    ent3.insert(0, new_text)



def format_data(event=None):
    text = ent2.get().replace("/", "")[:8]
    new_text = ""

    if event.keysym.lower() == "backspace": return

    for index in range(len(text)):

        if not text[index] in "0123456789": continue
        if index in [1, 3]:
            new_text += text[index] + "/"
        else:
            new_text += text[index]

    ent2.delete(0, "end")
    ent2.insert(0, new_text)

def format_telefone(event=None):
    text = ent4.get().replace("+", "").replace("(","").replace(")","")[:13]
    new_text = ""

    if event.keysym.lower() == "backspace": return

    for index in range(len(text)):

        if not text[index] in "0123456789": continue
        if index in [1]:
            new_text += text[index] + " "
        elif index in [7]:
            new_text += text[index] + "-"
        else:
            new_text += text[index]

    ent4.delete(0, "end")
    ent4.insert(0, new_text)

#-----------------

#funções
root.title('Windows Execute')
root.geometry('400x200+100+500')
root.minsize(width=620, height=350)
root.maxsize(width=1200, height=700)
root.config(bg=('dark grey'))
#configurando os frames
f1=Frame(root,background='Dark Grey',relief='raised',borderwidth=2)
f2=Frame(root,background='Dark Grey',relief='raised',borderwidth=2)
f3=Frame(root,background='Dark Grey',relief='raised',borderwidth=2)
f4=Frame(root,background='Dark Grey',relief='raised',borderwidth=2)

#configurações (extras)
OptionList = [
"Cis",
"Trans",
"Trans Não-Binário",
"Agênero",
"Outro"
]

variable = tk.StringVar(f1)
variable.set(OptionList[0])

opt = tk.OptionMenu(f1, variable, *OptionList)
opt.config(text='Gênero', font=('Arial 10'), background='Dark Grey')
genero=Label(f1,text='Gênero:', font=('Arial 14'), background='Dark Grey')
sexo=Label(f1,text='Sexo:', font='Arial 14', background='Dark Grey')
#salame

Masculino = tk.BooleanVar()
Masculino.set(True)
Feminino= tk.BooleanVar()
Feminino.set(True)
Masculino = tk.Checkbutton(f1, text='Masculino', var=Masculino, bg='Dark Grey',activebackground='Blue')
Feminino= tk.Checkbutton(f1, text='Feminino', var=Feminino, bg='Dark Grey',activebackground='Pink')


#configurando os frames
#f1
lb1=Label(f1,text='Dados Pessoais', font= 'Arial 20',bg='Dark Grey')
lb2=Label(f1,text='Nome:',font='Arial 14',bg='Dark Grey')
ent1=Entry(f1,font='Arial 14',bg='Dark Grey')
lb3=Label(f1, text='Data Nasc:',font='Arial 14',bg='Dark Grey')
ent2=Entry(f1,font='Arial 14',bg='Dark Grey')
ent2.bind("<KeyRelease>", format_data)
lb4=Label(f1, text='CPF:',font='Arial 14',bg='Dark Grey')
ent3=Entry(f1,font='Arial 14',bg='Dark Grey')
ent3.bind("<KeyRelease>", format_cpf)
lb5=Label(f1, text='Telefone:',font='Arial 14',bg='Dark Grey')
ent4=Entry(f1,font='Arial 14',bg='Dark Grey')
ent4.bind("<KeyRelease>", format_telefone)
#f2 -  rua,n, bairro, cidade,UF
lbl1=Label(f2,text='Endereço',font='Arial 20',bg='Dark Grey')
lbl2=Label(f2, text='Rua:', font='Arial 14',bg='Dark Grey')
en1=Entry(f2,font='Arial 14',bg='Dark Grey')
lbl3=Label(f2, text='Nº:', font='Arial 14',bg='Dark Grey')
en2=Entry(f2,font='Arial 14',bg='Dark Grey')
lbl4=Label(f2,text='Bairro:',font='Arial 14',bg='Dark Grey')
en3=Entry(f2,font='Arial 14',bg='Dark Grey')
lbl5=Label(f2,text='Cidade:',font='Arial 14',bg='Dark Grey')
en4=Entry(f2,font='Arial 14',bg='Dark Grey')
lbl6=Label(f2,text='UF:', font='Arial 14',bg='Dark Grey')
en5=Entry(f2,font='Arial 14',bg='Dark Grey')
#f3
btn=Button(f3, text='Salvar', font='Arial 11', background='light blue')
btn2=Button(f3, text='Imprimir', font='Arial 11', background='light blue')
#f4
lbla=Label(f4,text='User', font='Arial 14', background='Dark Grey')
em=Entry(f4,background='Dark Grey', insertbackground='Dark blue')
lblb=Label(f4,text='Senha', font='Arial 14', background='Dark Grey')
em2=Entry(f4, background='Dark Grey', insertbackground='Dark Blue', show='*')
bt=Button(f4, background='Light Blue', activebackground='Blue', text='Login')
#organizando
#f1
f1.pack(anchor=W)
lb1.grid(row=0)
lb2.grid(row=1)
ent1.grid(row=1,column=1)
lb3.grid(row=2)
ent2.grid(row=2,column=1)
lb4.grid(row=3)
ent3.grid(row=3,column=1)
lb5.grid(row=4)
ent4.grid(row=4,column=1)
lbl6.grid(row=5)
genero.grid(row=6,column=0)
opt.grid(row=6,column=1)
sexo.grid(row=7, column=0)
Masculino.grid(row=7, column=1)
Feminino.grid(row=7,column=2)
#f2
f2.pack(anchor=W)
lbl1.grid(row=0)
lbl2.grid(row=1)
en1.grid(row=1,column=1)
lbl3.grid(row=1,column=2)
en2.grid(row=1,column=3)
lbl4.grid(row=2)
en3.grid(row=2,column=1)
lbl5.grid(row=2)
en4.grid(row=2,column=1)
lbl6.grid(row=2,column=2)
en5.grid(row=2,column=3)
#f3
f3.pack(anchor=W)
btn.grid(row=0,column=0)
btn2.grid(row=0,column=1)
#f4
f4.pack
lbla.grid(row=2,column=1)
em.grid(row=2, column=2)
lblb.grid(row=3,column=1)
em2.grid(row=3,column=2)

root.mainloop()


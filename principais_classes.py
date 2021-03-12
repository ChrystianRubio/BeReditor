from tkinter import *
from tkinter import filedialog as Filedialog


class PrincipaisFunc:
   def __init__(self):
    
    self.root = Tk()
    self.root.title("BeReditor")


    self.mensagem = StringVar()
    self.mensagem.set("Bem vindo programador")
    
    
    self.monitor = Label(self.root, textvar=self.mensagem, justify="left") 
    self.monitor.pack(side="bottom")
    
    self.tamanho_da_fonte = int(14)
    self.cor_da_fonte = str("#ffffff")
    self.cor_de_fundo = str("#999966")

    self.texto = Text(self.root)
    self.texto.pack(fill="both", expand=1)
    self.texto.config(bd=0, padx=6, pady=4, font=('helvetica', self.tamanho_da_fonte), 
                                                  bg=self.cor_de_fundo, fg=self.cor_da_fonte)


    self.caminho = None


##################################################################################


   def abrir_arquivo(self):
    
    self.mensagem.set("Abrir arquivo")
    #self.mensagem.set(f'{caminho}')
    
    self.caminho = Filedialog.askopenfilename(initialdir=".",
                                              filetypes=(("Arquivos de texto", "*"),),
                                              title="Abrir arquivo de texto")

    if self.caminho:
      with open(self.caminho, 'r') as objeto_caminho:
        texto_digitado = objeto_caminho.read()
        self.texto.delete(1.0, END)
        self.texto.insert('insert', texto_digitado)
        self.mensagem.set(f">>> {self.caminho}")  


##################################################################################


   def abrir_arquivo_argumento(self):

    if self.caminho:
      with open(self.caminho, 'r') as objeto_caminho:
        texto_digitado = objeto_caminho.read()
        self.texto.delete(1.0, END)
        self.texto.insert('insert', texto_digitado)    
        self.mensagem.set(f">>> {self.caminho}")


##################################################################################

   def modificando_arquivo(self):
 
    texto_digitado = self.texto.get(1.0, "end-1c")
    with open(self.caminho, 'w+') as arquivo_objeto:
     arquivo_objeto.write(texto_digitado)
     self.mensagem.set("Gravado com sucesso")


##################################################################################


   def novo_arquivo(self):
    
    #self.caminho = None
          
    self.mensagem.set("Novo arquivo")
    self.texto.delete(1.0, END)



##################################################################################

   def salvar_como(self):
    self.mensagem.set("Salvar como")
          
    print(self.caminho)
          
    arquivo = Filedialog.asksaveasfile(title="Salvar como")
     
    if arquivo:
     self.caminho = arquivo.name
     self.modificando_arquivo()
    else:
     self.mensagem.set("Cancelado")


##################################################################################


   def salvar(self):

    self.mensagem.set("Salvo")
    
    if self.caminho: 
      self.modificando_arquivo()
    else:
      self.salvar_como()


##################################################################################


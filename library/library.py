# -*- coding: utf-8 -*-
# ---------------------------
# Y. Derfoufi -- CRMEF OUJDA
# ---------------------------
from tkinter import *
import os
savedFile = {1:""}
#======================================
# 1 - Création de la fenêtre principale
#======================================
class Win:
    def __init__(self,master,content):
        self.master = master
        self.content=content
    def create(self):
        self.master = Tk()
        self.master.title("Editeur de Texte")
        self.master.geometry("700x500")
        
     
    def add_text(self):
        self.content = Text(self.master)
        self.content.pack(expand=1,fill='both')
        
    def generate(self):
        self.master.mainloop()
        
#======================================
# 3 - Définition des actions des menus
#======================================
#------------------------------
# 3.1 - actions du menu Fichier
#-------------------------------
    def quitter(self):
        self.master.quit()
    def nouveau(self):
        
        os.popen("python main.py")
        
    def fopen(self):
        file = self.master.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select File",filetypes = (("Text Files","*.txt"),("all files","*.*")))
        
        fp = open(file,"r")
        r = fp.read()
        #print(r)
        self.content.insert(1.0,r)         
            
    def saveAs(self):
        # create save dialog
        fichier=self.master.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Enregistrer Sous\
        ",filetypes = (("Fichier Texte","*.txt"),("Tous les fichiers","*.*")))
        fichier = fichier + ".txt"
        
        savedFile[1] = str(fichier)
        f = open(fichier,"w")
        s = self.content.get("1.0",END)
        f.write(s) 
        f.close()
       
        
    def save(self):
        if(savedFile[1] ==""):
            self.saveAs()            
        else:
            f = open(savedFile[1],"w")
            s = self.content.get("1.0",END)
            f.write(s) 
            f.close() 
#------------------------------
# 3.2 - actions du menu Edition
#------------------------------
    def copy(self):
        self.content.clipboard_clear()
        self.content.clipboard_append(self.content.selection_get())
    
    def past(self):
        self.content.insert(INSERT, self.content.clipboard_get())
    
    def cut(self):
        self.copy()
        self.content.delete("sel.first","sel.last")    
#------------------------------
# 3.3 - actions du menu Outils
#------------------------------

#------------------------------
# 3.4 - actions du menu Aide
#------------------------------

#===========================
# 3 - Création des menus
#===========================
    def add_menu(self):
        # 1 - Création de la barre des menus
        menuBar = Menu(self.master)
        
        # 2 - Création du menu Fichier
        menuFichier = Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label = "Fichier", menu=menuFichier)
        menuFichier.add_command(label="Nouveau", command=self.nouveau)
        menuFichier.add_command(label="Ouvrir", command=self.fopen)
        menuFichier.add_command(label="Enregistrer", command=self.save)
        menuFichier.add_command(label="Enregistrer sous", command=self.saveAs)
        menuFichier.add_command(label="Quitter", command = self.quitter) 
        self.master.config(menu = menuBar)
        
        #3 - Création du Menu Edition
        menuEdition= Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label = "Edition ", menu=menuEdition)
        menuEdition.add_command(label="Annuler")
        menuEdition.add_command(label="Rétablir")
       
        menuEdition.add_command(label="Copier", command=self.copy)
        menuEdition.add_command(label="Couper", command = self.cut)
        menuEdition.add_command(label="Coller", command=self.past)
       
        # Création du Menu Options
        menuOutils = Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label = "Outils", menu = menuOutils)
        menuOutils.add_command(label="Préférences")
        
        # Création du Menu Aide
        menuAide = Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label = "Aide", menu = menuAide)
        menuAide.add_command(label="A propos")        
        
        
        




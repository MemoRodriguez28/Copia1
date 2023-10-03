import sys
from TAC import TAC

class Semantico:
    def __init__(self):
        self.variables = dict() #Variables
        self.labelsDeclaradas = set() #Labels
        self.labelsGoto = set() #Labels a las que se a saltado (GOTO)
        
    def abortar(self, mensaje):
        sys.exit("Error: " + mensaje)

    def revisarVariable(self, variable):
        if variable not in self.variables.keys(): #Revisando el lexema/nombre
            self.abortar("La variable no ha sido declarada: " + variable)
            
    def agregarVariable(self, variable):
        if variable not in self.variables.keys(): #Revisando si no se ha declarado esa variable
             self.variables[variable] = 'undefined'
    
    def actualizarVariable(self, valor):
        nom_variable = list(self.variables)[-1]
        self.revisarVariable(nom_variable)
        self.variables[nom_variable] = valor
        print(*TAC(self.variables[nom_variable]), sep='\n')
    
    def revisarLabelDeclarada(self, etiqueta):
        if etiqueta in self.labelsDeclaradas: 
            self.abortar("Ese Label (Etiqueta) ya existe: " + etiqueta)
                
    def agregarLabelDeclarada(self, etiqueta):
        self.labelsDeclaradas.add(etiqueta) #Agregando las labels declaradas
    
    def revisarLabelsGoto(self):
       for etiqueta in self.labelsGoto:
            if etiqueta not in self.labelsDeclaradas:
                self.abortar("Se intenta saltar a una etiqueta que no esta declarada " + etiqueta)
    
    def agregarLabelGoto(self, etiqueta):
        self.labelsGoto.add(etiqueta) #Agregando el salto
import random

class TPilha:
    def __init__(self):
      self.__PilhaN = []
      self.__PilhaP = []
        
#Adiciona o valor (value) ao final da pilha 
    def InserirPN(self, value):
      if(value == 0):
        self.__PilhaP.pop()
        self.__PilhaN.pop()
        print(f"Valor = 0,irei retirar um valor da das duas pilhas")
        
      elif(value % 2 == 0):
        print(f"valor {value} é par!")
        self.__PilhaP.append(value)
      else:
        print(f"valor {value} é impar!")
        self.__PilhaN.append(value)
        
#Remove o último valor da pilha
    def Retirar(self):
      self.__PilhaP.pop()
      self.__PilhaN.pop()
    
#imprime a pilha
    def Imprimir(self):
      print("Imprimir Pilha com Valor Par: ")
      print(f'structure: {self.__PilhaP}\n')
      print("Imprimir Pilha com Valor Impar: ")
      print(f'structure: {self.__PilhaN}\n')
      
def main():
    #Cria uma pilha 
    estrutura = TPilha()
    for _ in range(0, 20):
        estrutura.InserirPN(random.randint(0, 99))
    
    #Imprimir as pilhas
    estrutura.Imprimir()
    
    #Teste para remover valores
    estrutura.Retirar()
    estrutura.Retirar()

  #Imprimir as pilhas
    estrutura.Imprimir()

if __name__ == '__main__':
    main()
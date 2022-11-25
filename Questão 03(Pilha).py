class Estrutura:
  def __init__(self):
        self.__structure = []

#Criar Lista
  def Criar_Lista(self, value): 
    for i in value:
      self.__structure.append(i)
        
#Adiciona o valor (value) no final da Lista         
  def Adicionar_valor(self): 
    Elemento = int(input("Digite o Numero quer adicionar na lista: "))
    self.__structure.append(Elemento)
        
#Verificar elemento na Lista
  def Verificar_Elemento(self):
    Elemento = int(input("Digite o Numero queR vc ver se está na Lista: "))
    if(Elemento in self.__structure):
        print("O Elemento esta presente na Lista!\n")
    else:
         print("O Elemento não está presente!\n")
            
#Remove o Elemento da Lista
  def Remover(self):
    Elemento = int(input("Digite o Numero que vc quer Deletar: "))
    if(Elemento in self.__structure):
        return self.__structure.remove(Elemento)
    else:
        print("O Elemento não está presente!\n")
    
#imprime a Lista
  def Imprimir(self):
      print(f'\nstructure: {self.__structure}\n')
        
def main():
    
    #Cria uma pilha e utiliza os métodos show, pop e push
    Testeilhas = Estrutura()
    Vetor = [1,2,3,4,5,6,7]
    
    Testeilhas.Criar_Lista(Vetor)
    
    #Imprimir
    Testeilhas.Imprimir()
    
    #Pesquisar 
    Testeilhas.Verificar_Elemento()
    
    #remover valor
    Testeilhas.Remover()
    Testeilhas.Remover()
    
    #mprimir os valores  
    Testeilhas.Imprimir()
    
    #Adicionar Numero
    Testeilhas.Adicionar_valor()
    Testeilhas.Imprimir()

if __name__ == '__main__':
    main()
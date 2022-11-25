class TPilha1:

  def __init__(self):
    self.__TPilha1 = []

#Adiciona o valor (value) ao final da pilha

  def Inserir(self, value):
    self.__TPilha1.append(value)

#Remove o último valor da pilha

  def pop(self):
    return self.__TPilha1.pop()


#imprime a pilha

  def show(self):
    print("Imprimir Ordem ")
    print(f'structure: {self.__TPilha1}\n')

def main():
  #Cria uma pilha e utiliza os métodos show, pop e push
  Pilha1 = TPilha1()
  Pilha2 = TPilha1()
  
  #for _ in range(0, 15):
    #Pilha1.Inserir(random.randint(10, 99))
    #Pilha2.Inserir(random.randint(10, 99))
  Pilha1.Inserir(1)
  Pilha2.Inserir(1)

  #Imprimir os valores
  Pilha1.show()
  Pilha2.show()

  #Teste para remover valores
  #Pilha1.pop()
  #Pilha2.pop()
  
  #Teste para determinar se as duas Pilhas São Iguais
  if(Pilha1.show() == Pilha2.show()):
    print("Pilhas são iguais!")
  else:
    print("As Pilhas são Diferentes!")


if __name__ == '__main__':
  main()

import random

class TPilha:

  def __init__(self):
    self.__TPilha = []

#Adiciona o valor (value) ao final da pilha

  def Inserir(self, value):
    self.__TPilha.append(value)

#Remove o último valor da pilha

  def pop(self):
    return self.__TPilha.pop()


#imprime a pilha

  def show(self):
    print("Imprimir Ordem ")
    print(f'structure: {self.__TPilha}\n')

  def MaiorValor(self):
    print(f"O maior valor da pilha é : {max(self.__TPilha)}")


def main():
  #Cria uma pilha e utiliza os métodos show, pop e push
  estrutura = TPilha()

  for _ in range(0, 15):
    estrutura.Inserir(random.randint(10, 99))

  #Imprimir os valores
  estrutura.show()

  #Teste para remover valores
  estrutura.pop()
  estrutura.pop()

  #Imprimir os valores
  estrutura.show()

  #Imprimi o maior valor da Pilha
  estrutura.MaiorValor()

if __name__ == '__main__':
    main()

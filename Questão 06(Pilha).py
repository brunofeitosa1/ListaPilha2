import random
class TPilha:

  def __init__(self):
    self.__TPilha = []

#Adiciona o valor (value) ao final da pilha
  def InserirValorPar(self, value):
    if (value % 2 == 0):
      self.__TPilha.append(value)
    else:
      print(f"O valor {value} é impar,Não aceito valores Imparess!")

#Remove o último valor da pilha
  def pop(self):
    return self.__TPilha.pop()

#imprime a pilha
  def show(self):
    print("Imprimir Ordem ")
    print(f'structure: {self.__TPilha}\n')
    
def main():
  #Cria uma pilha e utiliza os métodos show, pop e push
  estrutura = TPilha()

  for _ in range(0, 15):
    estrutura.InserirValorPar(random.randint(10, 99))

  #Imprimir os valores
  estrutura.show()

  #Teste para remover valores
  estrutura.pop()
  estrutura.pop()

  #Imprimir os valores
  estrutura.show()


if __name__ == '__main__':
  main()

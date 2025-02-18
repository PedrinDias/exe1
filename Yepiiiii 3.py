''' Codigo para pedir pro usuario inserir 3 numeros diferentes em decimal/Float
      digite a n1(decimal)
      digite a n2(decimal)
      digite a n3(decimal)
'''
n1 = float(input("Escreva 1 numero: "))
n2 = float(input("Escreva 1 numero: "))
n3 = float(input("Escreva 1 numero: "))

'''  Os 3 numeros somando e dividindo pela quantidade de numeros existentes
      soma(decimal) = (n1 + n2 + n3)/ 3
      Media(decimal) = Soma / 3
'''
soma = (n1 + n2 + n3)/ 3

''' Condição para validar se a media dos 3 numeros sao maior ou menor que 7
    Caso esteje acima ou igual a 7 aprovado, caso esteje abaixo reprovado.
'''
if soma >= 7:
  print("Voce foi aprovado")
else:
  print("Voce foi reprovado")

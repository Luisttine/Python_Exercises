#ListaIII
#Atividade 1

n = int(input("Digite uma nota enre 0 e 10: "))

while n < 0 or n > 10:
    print("Sua nota não é válida!")
    n = int(input("Digite uma nota válida: "))
    
print(f"Sua nota {n} é válida!!")
    
#Atividade 2

usuario = input("Digite um nome de usuário: ")
senha = input("Digite uma senha: ")

while senha == usuario:
    print("A senha pode facilmente ser descoberta!! Tente outra.")
    senha = input("Digite uma senha: ")

print("Seu usuário e senha foram salvos.")

#Atividade 3

a = 80000
b = 200000
anos = 0

while a < b :
  a = a * 0.03 + a
  b = b * 0.015 + b
  anos = anos + 1

print(f"Serão necessários {anos} anos para A alcançar B.")

#Atividade 4

n = int(input('Digite o seu número: '))

a, b = 1, 1
i = 1

while i <= n-2:
  a, b = b, a + b
  i = i + 1

print (b)

#Atividade 5

a = int(input("Digite um dos valores a serem calculados o mdc: "))
b = int(input("Digite um dos valores a serem calculados o mdc: "))

while a % b != 0:
  a, b = b, a%b

print(f"O mdc de seu número é: {b}")

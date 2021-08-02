#Atividade 1

n1 = int(input("Insira o primeiro número inteiro: "))

n2 = int(input("Insira o segundo núemro inteiro: "))



print(n1+n2)



#Atividade 2


m = int(input("Insira um valor em metros: "))

mm = m*1000



print("O valor em metros inserido é igual a", mm, "milímetros")



#Atividade 3


d = int(input("Insira o número de dias: "))

h = int(input("insira o número de horas: "))

m = int(input("insira o número de minutos:"))

s = int(input("insira o número de segundos:"))



total = d*24*60*60 + h*60*60 + m*60 + s



print(total)



#Atividade 4


s = int(input("Digite seu salário: "))

a = int(input("Digite seu aumento em %: "))


aumento = s*(a/100)

sf = aumento+s



print("Seu aumento foi de: ",aumento)

print(“Seu novo salário é:”,sf)



#Atividade 5


p = float(input("Digite o preço da mercadoria: "))

d = int(input("Digite a porcentagem do desconto: "))


desconto = p*d/100

p_final = p-desconto



print(f"O valor do desconto é: {desconto:.2f}”)

print(f"O valor total a ser pago é: {p_final:.2f}” )



#Atividade 6


distancia = int(input("Digite a distância pretendida em km: "))

vm = float(input("Digite a sua velocidade média em km/h: "))

tempo = distancia/vm


if tempo < 1:
    h = int(tempo*60)

    print(“O tempo esperado de sua viagem é”, h, “minutos”)

else:

    print(“O tempo esperado de sua viagem é”, tempo, “horas”)



#Atividade 7


temperatura = int(input("Digite a temperatura em celsius: "))

fahrenheit = (9*temperatura/5) + 32



print("A temperatura convertida para fahrenheit é:",fahrenheit)



#Atividade 8


temperatura  = int(input(“Digite a temperatura em fahreinheit: “))

celsius = (temperatura - 23)*5/9



print(“A temperatura convertida para celsius é:”, celsius)



#Atividade 9


km = float(input(“Digite o km percorrido:”))

dias = int(input(“Digite os dias do aluguel do carro:”))


pkm = float(km*0.15)

pdias = float(dias*60.00)

pfinal = pkm+pdias



print(f”O valor total do aluguel é: R${pfinal:.2f}”)



#Atividade 10


quantidade = int(input(“Digite a quantidade de cigarros que você fuma por dia:”)

tempo = int(input(“Digite por quantos anos você fuma:”))

qfinal = tempo*quantidade*365

total = qfinal/144



print(f”Você tem um total de {total:.1f} dias a menos de vida.”)



#Atividade 11
 
print(len(str(2**1000000)))
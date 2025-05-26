print("-----------------------------------------")
nome_do_usuario = input("Qual é o seu nome?: ")


peso_kg = float(input("Informe seu peso: "))


altura_m = float(input("Informe sua altura: "))
print("-----------------------------------------")

IMC = peso_kg / (altura_m**2)
print(f'Valor do IMC: {IMC}')


if IMC >= 30.0 :
    print("Cuidado com a saude")
elif IMC < 30.0 :
    print("Tudo ok")



if IMC < 18.5:
    print ("Abaixo do peso")
elif 18.5 > IMC < 24.9:
    print ("Peso normal")
elif 25.0 > IMC < 29.9:
    print("Sobrepeso")
elif 30.0> IMC < 34.9:
    print ("Obesidade Grau I")
elif 35.0 > IMC < 39.9:
    print ("Obesidade Grau II")
elif IMC > 40.0 :
    print("Obesidade Grau III (mórbida)")
print("-----------------------------------------")